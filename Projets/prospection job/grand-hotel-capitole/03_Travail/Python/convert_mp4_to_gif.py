import os
import imageio

def convert_mp4_to_gif():
    base_path = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "video", "cerveau_4.2.mp4"))
    dest_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "video", "cerveau_42.gif"))

    if not os.path.exists(source_path):
        print(f"[X] Source introuvable : {source_path}")
        return

    print(f"[*] Lecture de la vidéo MP4 : {source_path}...")
    reader = imageio.get_reader(source_path)
    fps = reader.get_meta_data().get('fps', 10)
    
    print(f"[*] Conversion en GIF animé (FPS: {fps})...")
    writer = imageio.get_writer(dest_path, fps=fps, loop=0)
    
    for frame in reader:
        writer.append_data(frame)
        
    writer.close()
    print(f"[OK] GIF animé généré avec succès : {dest_path}")

if __name__ == "__main__":
    convert_mp4_to_gif()
