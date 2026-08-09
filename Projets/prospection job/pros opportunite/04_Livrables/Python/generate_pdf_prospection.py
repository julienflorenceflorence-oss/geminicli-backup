# -*- coding: utf-8 -*-
import os
import json
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

def generate_pdf():
    pdf_path = "Projets/prospection job/pros opportunite/04_Livrables/PDF/2026-08-10_LISTE_PROSPECTION_TOSCANE_OCCITANE.pdf"
    desktop_pdf = "/Users/admin/Desktop/2026-08-10_LISTE_PROSPECTION_TOSCANE_OCCITANE.pdf"
    
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4),
        rightMargin=1.0*cm,
        leftMargin=1.0*cm,
        topMargin=1.0*cm,
        bottomMargin=1.0*cm
    )

    story = []
    styles = getSampleStyleSheet()

    COLOR_BG_HEADER = colors.HexColor("#1E1B2E")
    COLOR_PURPLE = colors.HexColor("#6B21A8")
    COLOR_ALT_ROW = colors.HexColor("#F8FAFC")
    COLOR_BORDER = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.white
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#CBD5E1")
    )

    cell_name = ParagraphStyle(
        'CellName',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.HexColor("#0F172A")
    )

    cell_phone = ParagraphStyle(
        'CellPhone',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.HexColor("#2563EB")
    )

    cell_email = ParagraphStyle(
        'CellEmail',
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )

    cell_status = ParagraphStyle(
        'CellStatus',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        alignment=1,
        textColor=colors.HexColor("#CA8A04")
    )

    cell_notes = ParagraphStyle(
        'CellNotes',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#475569")
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
            Paragraph("<b>📊 DASHBOARD & MATRICE DE PROSPECTION HÉBERGEMENT & PRESTIGE</b>", title_style),
            Paragraph("<b>Julien FLORENCE</b><br/>Prospection Direction", ParagraphStyle('RightH', parent=subtitle_style, alignment=2))
        ],
        [
            Paragraph("11 Établissements Cibles (Toscane Occitane, Sète, Haute-Savoie Cordon)", subtitle_style),
            Paragraph("Mise à jour: 10/08/2026", ParagraphStyle('RightH2', parent=subtitle_style, alignment=2))
        ]
    ]

    header_table = Table(header_data, colWidths=[20.5*cm, 7.2*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_HEADER),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))

    story.append(header_table)
    story.append(Spacer(1, 0.3*cm))

    # 2. Table Data (11 Establishments)
    data = [
        [
            Paragraph("Établissement & Type", header_cell),
            Paragraph("Téléphone Contact", header_cell),
            Paragraph("Email & Web", header_cell),
            Paragraph("Statut Prospection", header_cell),
            Paragraph("Contact Sur Place & Notes", header_cell)
        ]
    ]

    venues = [
        {
            "name": "Domaine de la Durantie",
            "type": "Hébergement Groupe & Prestige",
            "loc": "Castelnau-de-Montmiral (Tarn)",
            "phone": "06 43 02 79 64\n05 63 33 21 00",
            "email": "reservations@durantie.com\nla-toscane-occitane.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Gérance Durantie\n• Domaine luxe groupe"
        },
        {
            "name": "Château Tauziès",
            "type": "Château Viticole & Séminaires",
            "loc": "Gaillac (Tarn)",
            "phone": "05 63 41 26 80",
            "email": "contact@chateaudetauzies.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Direction Tauziès\n• Séminaires & gîtes"
        },
        {
            "name": "Moulin de Trusse",
            "type": "Chambre d'Hôtes & Moulin",
            "loc": "Gaillac (Tarn)",
            "phone": "06 37 93 99 42",
            "email": "baptistempage@gmail.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Baptiste M.\n• Moulin de charme"
        },
        {
            "name": "La Maison de Clément",
            "type": "Gîte de Charme",
            "loc": "Castelnau-de-Montmiral",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Gîtes de France Tarn\n• Hébergement pittoresque"
        },
        {
            "name": "La Maison de Romain",
            "type": "Gîte d'Exception",
            "loc": "Puycelsi / Castelnau",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Gîtes de France Tarn\n• Maison de village d'exception"
        },
        {
            "name": "Ma vie là ! Au bord de l'eau",
            "type": "Gîte au Bord de l'Eau",
            "loc": "Lisle-sur-Tarn / Gaillac",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Gîtes de France Tarn\n• Cadre naturel bord de rivière"
        },
        {
            "name": "Hôtel Particulier Delga",
            "type": "Hôtel Particulier & Maison d'Hôtes",
            "loc": "Gaillac (Tarn)",
            "phone": "06 36 80 01 01",
            "email": "hoteldelga@gmail.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Propriétaires Delga\n• Demeure historique centre"
        },
        {
            "name": "Hôtel La Grande Roche",
            "type": "Hôtel & Domaine Lécusse",
            "loc": "Gaillac / Messac",
            "phone": "06 79 82 80 87",
            "email": "reception@chateaulecusse.fr",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Réception Lécusse\n• Domaine hôtelier"
        },
        {
            "name": "Hôtel du Château de Salettes",
            "type": "Hôtel 4* & Resto Gastronomique",
            "loc": "Cahuzac-sur-Vère",
            "phone": "05 63 33 60 60",
            "email": "salettes@chateaudesalettes.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "• Contact : Direction Générale\n• Château 4* vignoble"
        },
        {
            "name": "Appartement L'Étoile de Mer",
            "type": "Location de Vacances Bord de Mer",
            "loc": "Sète (Hérault 34)",
            "phone": "06 15 41 84 20",
            "email": "contact@location-sete.site\nlocation-sete.site",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "<b>• Contact Direct sur place : GISÈNE</b>\n• Appartement Sète plage"
        },
        {
            "name": "La Terrasse du Mont-Blanc",
            "type": "Chalet Prestige & Événementiel",
            "loc": "Cordon (Haute-Savoie 74)",
            "phone": "04 65 84 56 02 (Fixe)\n06 35 86 92 97 (Mobile)",
            "email": "contact@terrassedumontblanc.com\nterrassedumontblanc.com",
            "status": "[  ] À contacter\n[  ] 1er Appel\n[  ] RDV Fixé",
            "notes": "<b>• Contact Direct sur place : DAVID</b>\n• Chalet d'exception & séminaires"
        }
    ]

    for v in venues:
        name_cell = Paragraph(f"<b>{v['name']}</b><br/><font color='#64748B'>{v['type']}<br/>{v['loc']}</font>", cell_name)
        phone_cell = Paragraph(v['phone'].replace('\n', '<br/>'), cell_phone)
        email_cell = Paragraph(v['email'].replace('\n', '<br/>'), cell_email)
        status_cell = Paragraph(v['status'].replace('\n', '<br/>'), cell_status)
        notes_cell = Paragraph(v['notes'].replace('\n', '<br/>'), cell_notes)

        data.append([name_cell, phone_cell, email_cell, status_cell, notes_cell])

    col_widths = [6.2*cm, 3.8*cm, 5.5*cm, 3.5*cm, 8.7*cm]
    
    t = Table(data, colWidths=col_widths, repeatRows=1)
    
    t_style = [
        ('BACKGROUND', (0,0), (-1,0), COLOR_PURPLE),
        ('ALIGN', (0,0), (-1,0), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('PADDING', (0,0), (-1,-1), 4),
    ]

    for i in range(1, len(data)):
        if i % 2 == 0:
            t_style.append(('BACKGROUND', (0,i), (-1,i), COLOR_ALT_ROW))

    t.setStyle(TableStyle(t_style))
    story.append(t)

    doc.build(story)
    
    import shutil
    shutil.copyfile(pdf_path, desktop_pdf)
    print(f"✅ PDF Prospection 11 Établissements généré avec succès : {pdf_path}")
    print(f"✅ Copie Desktop disponible : {desktop_pdf}")

if __name__ == "__main__":
    generate_pdf()
