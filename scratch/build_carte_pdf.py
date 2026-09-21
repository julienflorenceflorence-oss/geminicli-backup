import os
from reportlab.lib.pagesizes import mm, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_business_card_pdf(output_path):
    # Standard business card size: 85mm x 54mm
    CARD_WIDTH = 85 * mm
    CARD_HEIGHT = 54 * mm
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=(CARD_WIDTH, CARD_HEIGHT),
        rightMargin=3 * mm,
        leftMargin=3 * mm,
        topMargin=3 * mm,
        bottomMargin=3 * mm
    )

    styles = getSampleStyleSheet()

    # Color Palette: Cyber Gold Executive
    DARK_BG = colors.HexColor("#0B0E14")
    GOLD = colors.HexColor("#D4AF37")
    GOLD_LIGHT = colors.HexColor("#FACC15")
    CYAN = colors.HexColor("#38BDF8")
    TEXT_LIGHT = colors.HexColor("#F8FAFC")
    TEXT_SUB = colors.HexColor("#94A3B8")
    CARD_BORDER = colors.HexColor("#334155")

    style_name = ParagraphStyle(
        'CardName',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=TEXT_LIGHT
    )

    style_title = ParagraphStyle(
        'CardTitle',
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8.5,
        textColor=GOLD
    )

    style_tagline = ParagraphStyle(
        'CardTagline',
        fontName='Helvetica',
        fontSize=5.5,
        leading=7.5,
        textColor=CYAN
    )

    style_contact = ParagraphStyle(
        'CardContact',
        fontName='Helvetica',
        fontSize=5.5,
        leading=7.5,
        textColor=TEXT_SUB
    )

    style_back_title = ParagraphStyle(
        'CardBackTitle',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=GOLD,
        alignment=1
    )

    style_back_sub = ParagraphStyle(
        'CardBackSub',
        fontName='Helvetica',
        fontSize=5.5,
        leading=7.5,
        textColor=TEXT_LIGHT,
        alignment=1
    )

    style_back_url = ParagraphStyle(
        'CardBackUrl',
        fontName='Helvetica-Bold',
        fontSize=5.5,
        leading=7.5,
        textColor=CYAN,
        alignment=1
    )

    story = []

    # --- RECTO (FRONT SIDE) ---
    photo_path = "/Users/admin/Desktop/geminicli-backup/julien_florence_photo.jpg"
    photo_img = None
    if os.path.exists(photo_path):
        photo_img = Image(photo_path, width=1.5*cm, height=1.8*cm)

    front_text = [
        Paragraph("<b>JULIEN FLORENCE</b>", style_name),
        Spacer(1, 1),
        Paragraph("DIRECTEUR COMMERCIAL • BU MANAGER", style_title),
        Paragraph("Management de Transition", style_title),
        Spacer(1, 2),
        Paragraph("Co-Fondateur QuestIA • Coach Fédéral FFHB", style_tagline),
        Spacer(1, 3),
        Paragraph("<b>Tél :</b> 06 61 74 75 73", style_contact),
        Paragraph("<b>Email :</b> julienflorence.florence@gmail.com", style_contact),
        Paragraph("<b>Ville :</b> Toulouse & Métropole", style_contact),
    ]

    if photo_img:
        front_table = Table([[photo_img, front_text]], colWidths=[1.7*cm, 6.0*cm])
        front_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(front_table)
    else:
        story.append(front_text)

    # --- VERSO (BACK SIDE WITH QR CODE) ---
    story.append(PageBreak())

    qr_path = "/Users/admin/Desktop/geminicli-backup/QR_Code_Carte_De_Visite.png"
    qr_img = None
    if os.path.exists(qr_path):
        qr_img = Image(qr_path, width=2.4*cm, height=2.4*cm)

    back_elements = [
        Paragraph("<b>SCANNEZ POUR ME CONTACTER</b>", style_back_title),
        Spacer(1, 2),
    ]
    if qr_img:
        back_elements.append(qr_img)
    back_elements.extend([
        Spacer(1, 2),
        Paragraph("Accès au Contact Direct vCard & CV Dashboard", style_back_sub),
        Paragraph("<b>julienflorenceflorence-oss.github.io/geminicli-backup/</b>", style_back_url)
    ])

    back_table = Table([[back_elements]], colWidths=[7.9*cm])
    back_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(back_table)

    doc.build(story)
    print("Business card PDF generated successfully:", output_path)

if __name__ == "__main__":
    from reportlab.lib.units import cm
    out_dir = "/Users/admin/Desktop/geminicli-backup/04_Livrables/PDF"
    os.makedirs(out_dir, exist_ok=True)
    p1 = os.path.join(out_dir, "Carte_De_Visite_Julien_Florence.pdf")
    p2 = "/Users/admin/Desktop/geminicli-backup/Carte_De_Visite_Julien_Florence.pdf"
    
    generate_business_card_pdf(p1)
    generate_business_card_pdf(p2)
