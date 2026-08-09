# -*- coding: utf-8 -*-
import os
import json
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

def generate_pdf():
    pdf_path = "Projets/prospection job/pros opportunite/04_Livrables/PDF/2026-08-10_LISTE_PROSPECTION_TOSCANE_OCCITANE.pdf"
    desktop_pdf = "/Users/admin/Desktop/2026-08-10_LISTE_PROSPECTION_TOSCANE_OCCITANE.pdf"
    
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    # Document Setup - Landscape A4 for wide table fit
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4),
        rightMargin=1.2*cm,
        leftMargin=1.2*cm,
        topMargin=1.2*cm,
        bottomMargin=1.2*cm
    )

    story = []
    styles = getSampleStyleSheet()

    # Custom Color Palette (Luxury Dark & Emerald Gold)
    COLOR_PRIMARY = colors.HexColor("#0C0A10")
    COLOR_PURPLE = colors.HexColor("#6B21A8")
    COLOR_GOLD = colors.HexColor("#CA8A04")
    COLOR_BG_HEADER = colors.HexColor("#1E1B2E")
    COLOR_ALT_ROW = colors.HexColor("#F8FAFC")
    COLOR_BORDER = colors.HexColor("#E2E8F0")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.white,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#CBD5E1")
    )

    cell_name = ParagraphStyle(
        'CellName',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor("#0F172A")
    )

    cell_sub = ParagraphStyle(
        'CellSub',
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#64748B")
    )

    cell_phone = ParagraphStyle(
        'CellPhone',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor("#2563EB")
    )

    cell_email = ParagraphStyle(
        'CellEmail',
        fontName='Helvetica',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.HexColor("#0F172A")
    )

    cell_status = ParagraphStyle(
        'CellStatus',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=1, # Center
        textColor=colors.HexColor("#CA8A04")
    )

    cell_notes = ParagraphStyle(
        'CellNotes',
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#94A3B8")
    )

    header_cell = ParagraphStyle(
        'HeaderCell',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white
    )

    # 1. Header Banner
    header_data = [
        [
            Paragraph("<b>📊 MATRICE DE PROSPECTION — TOSCANE OCCITANE</b>", title_style),
            Paragraph("<b>Julien FLORENCE</b><br/>Prospection Direction & Opportunités", ParagraphStyle('RightH', parent=subtitle_style, alignment=2))
        ],
        [
            Paragraph("Établissements & Hébergements de Prestige (Gaillac, Castelnau-de-Montmiral, Cahuzac-sur-Vère)", subtitle_style),
            Paragraph("Date: 10/08/2026", ParagraphStyle('RightH2', parent=subtitle_style, alignment=2))
        ]
    ]

    header_table = Table(header_data, colWidths=[20*cm, 7.3*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_HEADER),
        ('PADDING', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,1), (-1,1), 10),
    ]))

    story.append(header_table)
    story.append(Spacer(1, 0.4*cm))

    # 2. Main Prospection Table Data
    data = [
        [
            Paragraph("Établissement & Type", header_cell),
            Paragraph("Téléphone", header_cell),
            Paragraph("Email Contact", header_cell),
            Paragraph("Statut Prospection", header_cell),
            Paragraph("Espace Commentaires & Prise de Notes", header_cell)
        ]
    ]

    venues = [
        {
            "name": "Domaine de la Durantie",
            "type": "Hébergement Groupe & Prestige",
            "loc": "Castelnau-de-Montmiral",
            "phone": "06 43 02 79 64\n05 63 33 21 00",
            "email": "reservations@durantie.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Responsable / Gérant :\n• Notes :"
        },
        {
            "name": "Château Tauziès",
            "type": "Château Viticole & Séminaires",
            "loc": "Gaillac",
            "phone": "05 63 41 26 80",
            "email": "contact@chateaudetauzies.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Responsable / Gérant :\n• Notes :"
        },
        {
            "name": "Moulin de Trusse",
            "type": "Chambre d'Hôtes & Moulin",
            "loc": "Gaillac",
            "phone": "06 37 93 99 42",
            "email": "baptistempage@gmail.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Responsable / Gérant :\n• Notes :"
        },
        {
            "name": "La Maison de Clément",
            "type": "Gîte de Charme",
            "loc": "Castelnau-de-Montmiral",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Propriétaire en direct :\n• Notes :"
        },
        {
            "name": "La Maison de Romain",
            "type": "Gîte d'Exception",
            "loc": "Puycelsi / Castelnau",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Propriétaire en direct :\n• Notes :"
        },
        {
            "name": "Ma vie là ! Au bord de l'eau",
            "type": "Gîte de Charme au Bord de l'Eau",
            "loc": "Lisle-sur-Tarn / Gaillac",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Propriétaire en direct :\n• Notes :"
        },
        {
            "name": "Hôtel Particulier Delga",
            "type": "Hôtel Particulier & Maison d'Hôtes",
            "loc": "Gaillac",
            "phone": "06 36 80 01 01",
            "email": "hoteldelga@gmail.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Direction / Propriétaire :\n• Notes :"
        },
        {
            "name": "Hôtel La Grande Roche",
            "type": "Hôtel & Domaine Lécusse",
            "loc": "Gaillac / Messac",
            "phone": "06 79 82 80 87",
            "email": "reception@chateaulecusse.fr",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Direction Hôtel :\n• Notes :"
        },
        {
            "name": "Hôtel du Château de Salettes",
            "type": "Hôtel 4* & Resto Gastronomique",
            "loc": "Cahuzac-sur-Vère",
            "phone": "05 63 33 60 60",
            "email": "salettes@chateaudesalettes.com",
            "status": "[  ] À contacter\n[  ] Premier appel\n[  ] RDV fixé",
            "notes": "• Direction Général / Restauration :\n• Notes :"
        }
    ]

    for v in venues:
        name_cell = Paragraph(f"<b>{v['name']}</b><br/><font color='#64748B'>{v['type']} ({v['loc']})</font>", cell_name)
        phone_cell = Paragraph(v['phone'].replace('\n', '<br/>'), cell_phone)
        email_cell = Paragraph(f"<a href='mailto:{v['email']}'>{v['email']}</a>", cell_email)
        status_cell = Paragraph(v['status'].replace('\n', '<br/>'), cell_status)
        notes_cell = Paragraph(v['notes'].replace('\n', '<br/>'), cell_notes)

        data.append([name_cell, phone_cell, email_cell, status_cell, notes_cell])

    # Table Column Widths (Total ~27.3 cm to fit Landscape A4)
    col_widths = [6.5*cm, 3.8*cm, 5.5*cm, 3.5*cm, 8.0*cm]
    
    t = Table(data, colWidths=col_widths, repeatRows=1)
    
    t_style = [
        ('BACKGROUND', (0,0), (-1,0), COLOR_PURPLE),
        ('ALIGN', (0,0), (-1,0), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('PADDING', (0,0), (-1,-1), 6),
    ]

    # Alternating row colors
    for i in range(1, len(data)):
        if i % 2 == 0:
            t_style.append(('BACKGROUND', (0,i), (-1,i), COLOR_ALT_ROW))

    t.setStyle(TableStyle(t_style))
    story.append(t)

    # Build Document
    doc.build(story)
    
    # Copy to Desktop
    import shutil
    shutil.copyfile(pdf_path, desktop_pdf)
    print(f"✅ PDF Prospection généré avec succès : {pdf_path}")
    print(f"✅ Copie Desktop disponible : {desktop_pdf}")

if __name__ == "__main__":
    generate_pdf()
