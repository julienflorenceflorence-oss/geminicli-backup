import sys
import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

def generate_cv_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.2*cm,
        bottomMargin=1.2*cm
    )

    styles = getSampleStyleSheet()
    
    DARK_BLUE = colors.HexColor("#0B0E14")
    GOLD = colors.HexColor("#B89628")
    CYAN = colors.HexColor("#0284C7")
    TEXT_DARK = colors.HexColor("#1E293B")
    TEXT_MUTED = colors.HexColor("#64748B")
    BG_LIGHT = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#E2E8F0")

    style_name = ParagraphStyle(
        'CVName',
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=DARK_BLUE
    )
    
    style_title = ParagraphStyle(
        'CVTitle',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=GOLD
    )
    
    style_contact = ParagraphStyle(
        'CVContact',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_MUTED,
        alignment=2
    )

    style_section_heading = ParagraphStyle(
        'CVSectionHeading',
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=DARK_BLUE,
        spaceAfter=5
    )

    style_body = ParagraphStyle(
        'CVBody',
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=TEXT_DARK
    )

    style_bullet = ParagraphStyle(
        'CVBullet',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_DARK,
        leftIndent=8
    )

    story = []

    # PHOTO + HEADER TABLE
    photo_path = "/Users/admin/Desktop/geminicli-backup/julien_florence_photo.jpg"
    photo_img = None
    if os.path.exists(photo_path):
        photo_img = Image(photo_path, width=2.4*cm, height=2.8*cm)

    header_left_text = [
        Paragraph("JULIEN FLORENCE", style_name),
        Spacer(1, 2),
        Paragraph("DIRECTEUR COMMERCIAL • BU MANAGER • MANAGEMENT DE TRANSITION", style_title),
        Spacer(1, 3),
        Paragraph("Parcours Authentique (2000-2026) | Hôtellerie Luxe, Immobilier, BU & Coach FFHB", style_body)
    ]

    if photo_img:
        header_left_table = Table([[photo_img, header_left_text]], colWidths=[2.8*cm, 8.2*cm])
        header_left_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        header_left = header_left_table
    else:
        header_left = header_left_text
    
    header_right = [
        Paragraph("<b>Tél :</b> 06 61 74 75 73", style_contact),
        Paragraph("<b>Email :</b> julienflorence.florence@gmail.com", style_contact),
        Paragraph("<b>Localisation :</b> Toulouse (31)", style_contact),
        Paragraph("<b>LinkedIn :</b> linkedin.com/in/julien-florence-2536a083", style_contact),
        Paragraph("<b>Dashboard :</b> github.io/geminicli-backup", style_contact)
    ]

    header_table = Table([[header_left, header_right]], colWidths=[11*cm, 7*cm])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))

    story.append(header_table)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD, spaceAfter=10))

    # EXECUTIVE SUMMARY
    story.append(Paragraph("PROFIL EXÉCUTIF & POSTURE ENTJ-A", style_section_heading))
    summary_text = (
        "Parcours riche et exigeant combinant l'excellence du terrain, l'hôtellerie de luxe à l'international "
        "(Sommelier Palace en Irlande), la négociation immobilière de biens d'exception, la gestion de centres de profit "
        "(Gestionnaire RAS, +35% CA) et la direction du développement (Happy House / Rocket School, Coestia). "
        "Titulaire du diplôme de Coach Fédéral de Handball (FFHB), j'incarne une posture de Manager-Coach axée sur l'analyse "
        "systémique des causes (Facilité × Confiance × Effet), l'intelligence relationnelle (DISC/PCM) et l'accélération par l'IA."
    )
    story.append(Paragraph(summary_text, style_body))
    story.append(Spacer(1, 10))

    # REAL TIMELINE (2000 - 2026)
    story.append(Paragraph("PARCOURS PROFESSIONNEL REEL (2000 - 2026)", style_section_heading))

    story.append(Paragraph("<b>2024 - 2026 | Fondateur & Dirigeant Exécutif — Coestia / QuestIA</b> (Toulouse)", style_body))
    story.append(Paragraph("• Intelligence Commerciale, automatisation n8n, CRM psychométrique DISC/PCM et conseil stratégique.", style_bullet))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>2023 - 2024 | Directeur du Développement & Sales Strategy — Happy House / Rocket School</b>", style_body))
    story.append(Paragraph("• Structuration de la Sales Engine, animation force de vente, coaching SDR (cold calling) & budget zéro.", style_bullet))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>2018 - 2023 | Gestionnaire Centre de Profit & Directeur d'Exploitation — RAS / Restauration</b>", style_body))
    story.append(Paragraph("• Management de 15 à 50 collaborateurs, pilotage financier du P&L, maître d'hôtel & croissance de +35% CA.", style_bullet))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>2010 - 2018 | Sommelier Palace (Irlande) & Négociateur Immobilier d'Exception</b>", style_body))
    story.append(Paragraph("• Hôtellerie de luxe internationale (Irlande), maîtrise des codes comportementaux haut de gamme & transaction immobilière.", style_bullet))
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>2000 - 2010 | Joueur National 3 (N3) & Coach Fédéral de Handball</b> (FFHB)", style_body))
    story.append(Paragraph("• Diplôme de Coach Fédéral FFHB, compétition N3, gestion de matchs haute intensité & cohésion d'équipe.", style_bullet))
    story.append(Spacer(1, 10))

    # DIPLOMES ET CERTIFICATIONS
    story.append(Paragraph("DIPLÔMES & CERTIFICATIONS", style_section_heading))
    
    diplomas_data = [
        [
            Paragraph("<b>Diplôme de Coach Fédéral</b><br/>FFHB (Handball National)", style_body),
            Paragraph("<b>Master Européen / Executive</b><br/>Management & Stratégie (Bac+5)", style_body),
            Paragraph("<b>Psychométrie DISC & PCM</b><br/>Certifié Profiling Commercial", style_body),
        ],
        [
            Paragraph("<b>Licence Joueur N3 Handball</b><br/>Compétition Nationale", style_body),
            Paragraph("<b>Sommelier Palace (Irlande)</b><br/>Hôtellerie Luxe & Immobilier", style_body),
            Paragraph("<b>IA & Automation Workflows</b><br/>n8n, Scraping & CRM Sales", style_body),
        ]
    ]

    diplomas_table = Table(diplomas_data, colWidths=[6*cm, 6*cm, 6*cm])
    diplomas_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(diplomas_table)

    doc.build(story)
    print("Authentic PDF build complete:", output_path)

if __name__ == "__main__":
    out_dir = "/Users/admin/Desktop/geminicli-backup/04_Livrables/PDF"
    os.makedirs(out_dir, exist_ok=True)
    out1 = os.path.join(out_dir, "Julien_Florence_CV_Direction_Commerciale.pdf")
    out2 = "/Users/admin/Desktop/geminicli-backup/Julien_Florence_CV_Direction_Commerciale.pdf"
    
    generate_cv_pdf(out1)
    generate_cv_pdf(out2)
