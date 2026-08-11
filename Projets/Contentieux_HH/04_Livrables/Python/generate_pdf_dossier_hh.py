# -*- coding: utf-8 -*-
import os
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

def generate_pdf():
    pdf_path = "Projets/Contentieux_HH/04_Livrables/PDF/2026-08-11_DOSSIER_RECOURS_HAPPY_HOUSE.pdf"
    desktop_pdf = "/Users/admin/Desktop/2026-08-11_DOSSIER_RECOURS_HAPPY_HOUSE.pdf"
    
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm
    )

    story = []
    styles = getSampleStyleSheet()

    COLOR_BG_HEADER = colors.HexColor("#1E1B2E")
    COLOR_PURPLE = colors.HexColor("#6B21A8")
    COLOR_RED = colors.HexColor("#DC2626")
    COLOR_ALT_ROW = colors.HexColor("#F8FAFC")
    COLOR_BORDER = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.white
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#CBD5E1")
    )

    h2_style = ParagraphStyle(
        'H2Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=COLOR_PURPLE,
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1E293B")
    )

    bold_body = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    header_cell = ParagraphStyle(
        'HeaderCell',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.white
    )

    # 1. Header Banner
    header_data = [
        [
            Paragraph("<b>⚖️ AUDIT STRATÉGIQUE & CONTENTIEUX SALARIAL — HAPPY HOUSE</b>", title_style),
            Paragraph("<b>Julien FLORENCE</b><br/>Affaire Contentieux_HH", ParagraphStyle('RightH', parent=subtitle_style, alignment=2))
        ],
        [
            Paragraph("Société ciblée : HAPPY HOUSE SAS (SIRET : 879 944 437 000 26) | Convention : IDCC 1527", subtitle_style),
            Paragraph("Date : 11/08/2026", ParagraphStyle('RightH2', parent=subtitle_style, alignment=2))
        ]
    ]

    header_table = Table(header_data, colWidths=[12.5*cm, 5.5*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_HEADER),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))

    story.append(header_table)
    story.append(Spacer(1, 0.4*cm))

    # 2. Executive Summary Box
    story.append(Paragraph("<b>1. CONTEXTE & INVIOLABILITÉ DES DROITS (IDCC 1527)</b>", h2_style))
    p1 = ("L'entreprise HAPPY HOUSE SAS relève de plein droit de la <b>Convention Collective Nationale de l'Immobilier (IDCC 1527)</b>. "
          "La mention obligatoire figurant sur les bulletins de paie vaut présomption irréfragable de son application (<i>Cass. soc., 15 nov. 2007</i>). "
          "Un alternant / apprenti est un salarié de droit commun (<i>Art. L6221-1 & L6222-23 du Code du travail</i>) et bénéficie des mêmes droits conventionnels.<br/><br/>"
          "<b>RÈGLE STRICTE SUR LA RÉTENTION :</b> L'article <b>L3251-1 du Code du travail</b> interdit formellement à un employeur de retenir un salaire ou "
          "de bloquer les documents de fin de contrat (bulletins, certificat de travail, attestation France Travail) pour exiger la remise d'un document ou la restitution de matériel. "
          "Subordonner la paie à une contrepartie constitue un <b>trouble manifestement illicite</b> (<i>Art. R1455-6</i>) sanctionné en référé sous astreinte.")
    story.append(Paragraph(p1, body_style))
    story.append(Spacer(1, 0.3*cm))

    # 3. Claims Chiffrage Table
    story.append(Paragraph("<b>2. TABLEAU RECAPITULATIF DES CRÉANCES SALARIALES CHIFFRABLES</b>", h2_style))
    
    table_data = [
        [
            Paragraph("Poste de Créance", header_cell),
            Paragraph("Fondement Juridique", header_cell),
            Paragraph("Formule & Détails", header_cell),
            Paragraph("Montant Estimé", header_cell)
        ],
        [
            Paragraph("<b>13e Mois Conventionnel</b>", body_style),
            Paragraph("Art. 38 IDCC 1527", body_style),
            Paragraph("1 mois brut / an au prorata de la présence (non inclus SMIC)", body_style),
            Paragraph("<b>1 872,14 €</b>", bold_body)
        ],
        [
            Paragraph("<b>Ajustement Grille Branche</b>", body_style),
            Paragraph("Art. 37 / Avenant 104-110", body_style),
            Paragraph("Minimum annuel calculé sur 13 mois (Niveau E1 : 23 424 €)", body_style),
            Paragraph("<b>1 157,76 €</b>", bold_body)
        ],
        [
            Paragraph("<b>Frais & Matériel Télétravail</b>", body_style),
            Paragraph("Barème URSSAF 2026", body_style),
            Paragraph("Allocation Télétravail (55€/mois) + Matériel info (55,20€/mois)", body_style),
            Paragraph("<b>1 322,40 €</b>", bold_body)
        ],
        [
            Paragraph("<b>Indemnité Occupation Domicile</b>", body_style),
            Paragraph("Cass. soc. 19/03/2025", body_style),
            Paragraph("Compensation immixtion vie privée (85 € / mois sur 12 mois)", body_style),
            Paragraph("<b>1 020,00 €</b>", bold_body)
        ],
        [
            Paragraph("<b>TOTAL DES CRÉANCES</b>", header_cell),
            Paragraph("Rappels chiffrables", header_cell),
            Paragraph("Délai de prescription : 3 ans (salaires) / 2 ans (frais)", header_cell),
            Paragraph("<b>5 372,30 €</b>", header_cell)
        ]
    ]

    t_claims = Table(table_data, colWidths=[4.2*cm, 4.0*cm, 6.8*cm, 3.0*cm])
    t_claims.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PURPLE),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('PADDING', (0,0), (-1,-1), 5),
        ('BACKGROUND', (0,-1), (-1,-1), COLOR_BG_HEADER),
    ]))
    story.append(t_claims)
    story.append(Spacer(1, 0.4*cm))

    # 4. Action Plan Table
    story.append(Paragraph("<b>3. PLAN D'ACTION OPÉRATIONNEL EN 4 ÉTAPES</b>", h2_style))
    
    plan_data = [
        [Paragraph("Étape", header_cell), Paragraph("Action Concrète", header_cell), Paragraph("Canal & Objectif", header_cell)],
        [
            Paragraph("<b>Étape 1</b><br/><i>Immédiat</i>", body_style),
            Paragraph("• Inscription France Travail en ligne<br/>• Export & horodatage des preuves (mails, SMS, Slack)<br/>• Blocage de toute signature de solde de tout compte", body_style),
            Paragraph("Figer les preuves et sécuriser l'ouverture des droits chômage sans délai.", body_style)
        ],
        [
            Paragraph("<b>Étape 2</b><br/><i>Semaine 1</i>", body_style),
            Paragraph("• Envoi du Mail 1 de régularisation amiable (uniquement rappels chiffrables)<br/>• Proposition d'échéancier en 2 versements", body_style),
            Paragraph("Obtenir un accord rapide et retirer l'argument de trésorerie de l'employeur.", body_style)
        ],
        [
            Paragraph("<b>Étape 3</b><br/><i>J+15</i>", body_style),
            Paragraph("• Lettre Recommandée AR valant Mise en Demeure officielle<br/>• Signalement gratuit à l'Inspection du Travail (DREETS)", body_style),
            Paragraph("Faire courir les intérêts de retard au taux légal et forcer la conformité.", body_style)
        ],
        [
            Paragraph("<b>Étape 4</b><br/><i>J+30</i>", body_style),
            Paragraph("• Saisine de la Formation de Référé du Conseil de Prud'hommes", body_style),
            Paragraph("Ordonnance de paiement sous astreinte sous Art. R1455-6 et R1455-7.", body_style)
        ]
    ]

    t_plan = Table(plan_data, colWidths=[2.5*cm, 9.5*cm, 6.0*cm])
    t_plan.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PURPLE),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_plan)

    doc.build(story)
    
    import shutil
    shutil.copyfile(pdf_path, desktop_pdf)
    print(f"✅ PDF Dossier Contentieux HH généré avec succès : {pdf_path}")
    print(f"✅ Copie disponible sur le Bureau Mac : {desktop_pdf}")

if __name__ == "__main__":
    generate_pdf()
