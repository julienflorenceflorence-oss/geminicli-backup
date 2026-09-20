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
    
    # Custom Colors
    DARK_BLUE = colors.HexColor("#0B0E14")
    GOLD = colors.HexColor("#B89628")
    CYAN = colors.HexColor("#0284C7")
    TEXT_DARK = colors.HexColor("#1E293B")
    TEXT_MUTED = colors.HexColor("#64748B")
    BG_LIGHT = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#E2E8F0")

    # Custom Typography Styles
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
        alignment=2 # Right aligned
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
        Paragraph("26 Ans de Trajectoire (2000-2026) | Culture P&L & ROI | Coach Fédéral FFHB", style_body)
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
        "Manager chevronné (2000-2026), fort de 20 ans d'expérience dans la création, la direction et "
        "l'expansion de centres de profit. Alliant rigueur analytique, culture du résultat P&L et posture de "
        "Manager-Coach issue du sport collectif au niveau national (Handball N3 & Coach Fédéral FFHB), j'interviens sur la Direction Commerciale, "
        "la gestion de Business Unit ou le Management de Transition. Expert en stratégie Go-to-Market, "
        "prospection B2B augmentée par l'Intelligence Artificielle et psychométrie commerciale (DISC/PCM)."
    )
    story.append(Paragraph(summary_text, style_body))
    story.append(Spacer(1, 10))

    # PARCOURS CHRONOLOGIQUE COMPLET (2000 - 2026)
    story.append(Paragraph("PARCOURS PROFESSIONNEL (2000 - 2026)", style_section_heading))

    story.append(Paragraph("<b>2024 - 2026 | Fondateur & Dirigeant Exécutif — Coestia / QuestIA</b> (Toulouse)", style_body))
    story.append(Paragraph("• Développement d'outils d'Intelligence Commerciale, workflows CRM et accompagnement des PME/ETI.", style_bullet))
    story.append(Paragraph("• Conception de pipelines de prospection B2B augmentés par l'IA et le profiling relationnel DISC/PCM.", style_bullet))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>2018 - 2024 | Business Unit Manager & Directeur d'Exploitation — CHR / Services</b> (Occitanie)", style_body))
    story.append(Paragraph("• Pilotage complet de l'EBITDA et du P&L, management direct de 15 à 50 collaborateurs.", style_bullet))
    story.append(Paragraph("• Croissance de +35% du chiffre d'affaires par restructuration de l'offre et dynamisation commerciale.", style_bullet))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>2012 - 2018 | Responsable du Développement Commercial & Grands Comptes</b> (Grand Sud-Ouest)", style_body))
    story.append(Paragraph("• Déploiement de stratégies Go-to-Market, négociation de contrats nationaux et structuration de la force de vente.", style_bullet))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>2006 - 2012 | Manager de Terrain & Chef de Ventes Operations</b> (France)", style_body))
    story.append(Paragraph("• Recrutement, formation et coaching terrain des équipes commerciales, pilotage des objectifs mensuels CA.", style_bullet))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>2000 - 2006 | Joueur National 3 (N3) & Entraîneur / Coach Fédéral Handball</b> (FFHB)", style_body))
    story.append(Paragraph("• Pratique du handball haut niveau (N3), coaching d'équipes en compétition, résilience et cohésion collective.", style_bullet))
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
            Paragraph("<b>Licence Joueur N3 Handball</b><br/>Championnat de France", style_body),
            Paragraph("<b>Certification IA & Automation</b><br/>Workflows CRM & Prompting", style_body),
            Paragraph("<b>Culture Management P&L</b><br/>20 Ans d'Expérience Exécutive", style_body),
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
    print("Updated PDF build complete:", output_path)

if __name__ == "__main__":
    out_dir = "/Users/admin/Desktop/geminicli-backup/04_Livrables/PDF"
    os.makedirs(out_dir, exist_ok=True)
    out1 = os.path.join(out_dir, "Julien_Florence_CV_Direction_Commerciale.pdf")
    out2 = "/Users/admin/Desktop/geminicli-backup/Julien_Florence_CV_Direction_Commerciale.pdf"
    
    generate_cv_pdf(out1)
    generate_cv_pdf(out2)
