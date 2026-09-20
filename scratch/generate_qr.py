import qrcode
import os
from PIL import Image

def generate_qr(url, out_path_png):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#0F1117", back_color="#FFFFFF").convert('RGB')
    img.save(out_path_png)
    print("QR Code generated successfully:", out_path_png)

if __name__ == "__main__":
    target_url = "https://julienflorenceflorence-oss.github.io/geminicli-backup/"
    
    out_dir = "/Users/admin/Desktop/geminicli-backup/04_Livrables/Images"
    os.makedirs(out_dir, exist_ok=True)
    
    p1 = os.path.join(out_dir, "QR_Code_Carte_De_Visite.png")
    p2 = "/Users/admin/Desktop/geminicli-backup/QR_Code_Carte_De_Visite.png"
    
    generate_qr(target_url, p1)
    generate_qr(target_url, p2)
