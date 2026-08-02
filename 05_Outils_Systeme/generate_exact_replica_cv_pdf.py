# -*- coding: utf-8 -*-
import os
import sys
import io

sys.path.insert(0, '/Users/admin/Library/Python/3.9/lib/python/site-packages')
import pypdf
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def modify_original_pdf():
    # Source PDF (Exact original uploaded by user)
    pdf_path = '/Users/admin/.gemini/antigravity/brain/3b3f54ca-b09a-4ea4-9dc8-59a0af5a76aa/.user_uploaded/media__1785535478616.pdf'
    reader = pypdf.PdfReader(pdf_path)
    base_page = reader.pages[0]
    
    # Overlay Canvas matching exact dimensions
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(594.96, 841.92))
    
    bg_main = colors.HexColor('#0B0C10')
    text_white = colors.HexColor('#F8FAFC')
    text_gray = colors.HexColor('#E2E8F0')
    
    # Cover old subtitle & old presentation text area completely (y=565 to y=775 pt)
    can.setFillColor(bg_main)
    can.setStrokeColor(bg_main)
    can.rect(195, 565, 395, 210, fill=1, stroke=0)
    
    # 1. New Subtitle (Exactly DIRECTEUR D'HÔTEL HYBRIDE)
    can.setFillColor(text_white)
    can.setFont('Helvetica-Bold', 9.5)
    can.drawString(205, 764, '| DIRECTEUR D\'HOTEL HYBRIDE')
    
    # 2. New Presentation Text
    p_lines = [
        "Directeur d'Hotel Hybride fort de 25 ans d'experience combinant la rigueur",
        "operationnelle et l'excellence du service de prestige (Palaces 5* & etoiles) au pilotage",
        "de centres de profit, Revenue Management et virage MICE B2B. Expert de l'evenementiel",
        "et du F&B, je suis operationnel pour piloter le site JOST Bordeaux Gare Saint-Jean."
    ]
    
    can.setFillColor(text_gray)
    can.setFont('Helvetica', 8.5)
    
    y = 744
    for line in p_lines:
        can.drawString(205, y, line)
        y -= 13.5
        
    # Clickable Hyperlinks on 4 buttons
    buttons_links = [
        ("tel:0661747573", 15, 600, 175, 625),
        ("mailto:julienflorence.florence@gmail.com", 15, 565, 175, 590),
        ("https://linkedin.com/in/alban-ruggiero/", 15, 530, 175, 555),
        ("https://github.com/julienflorenceflorence-oss/geminicli-backup/tree/main/Projets/prospection%20job/jost-hotel-bordeaux/04_Livrables/PDF", 15, 495, 175, 520)
    ]
    
    for url, x1, y1, x2, y2 in buttons_links:
        can.linkURL(url, (x1, y1, x2, y2), relative=0)
        
    can.save()
    
    packet.seek(0)
    overlay_reader = pypdf.PdfReader(packet)
    overlay_page = overlay_reader.pages[0]
    
    # Merge overlay onto base page
    base_page.merge_page(overlay_page)
    
    writer = pypdf.PdfWriter()
    writer.add_page(base_page)
    
    out_file = 'Projets/prospection job/jost-hotel-bordeaux/04_Livrables/PDF/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.pdf'
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'wb') as f:
        writer.write(f)
        
    # Also save to Desktop and Desktop/JOST folder
    desktop_jost = '/Users/admin/Desktop/JOST/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.pdf'
    desktop_root = '/Users/admin/Desktop/CV_Julien_Florence_JOST_Bordeaux.pdf'
    os.makedirs(os.path.dirname(desktop_jost), exist_ok=True)
    with open(desktop_jost, 'wb') as f:
        writer.write(f)
    with open(desktop_root, 'wb') as f:
        writer.write(f)
        
    print("✅ Titre et texte de présentation mis à jour avec succès !")

if __name__ == "__main__":
    modify_original_pdf()
