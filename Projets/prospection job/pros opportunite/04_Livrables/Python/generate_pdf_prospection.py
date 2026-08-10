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
        rightMargin=0.8*cm,
        leftMargin=0.8*cm,
        topMargin=0.8*cm,
        bottomMargin=0.8*cm
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

    cell_name = ParagraphStyle(
        'CellName',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )

    cell_addr = ParagraphStyle(
        'CellAddr',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#334155")
    )

    cell_phone = ParagraphStyle(
        'CellPhone',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#2563EB")
    )

    cell_email = ParagraphStyle(
        'CellEmail',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
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
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#1E293B")
    )

    header_cell = ParagraphStyle(
        'HeaderCell',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.white
    )

    # Header Banner
    header_data = [
        [
            Paragraph("<b>📊 MATRICE OPÉRATIONNELLE DE PROSPECTION & NOTES DE SUIVI</b>", title_style),
            Paragraph("<b>Julien FLORENCE</b><br/>Prospection Direction", ParagraphStyle('RightH', parent=subtitle_style, alignment=2))
        ],
        [
            Paragraph("11 Établissements avec Téléphones, Emails, Adresses Postales & Notes Réelles de Terrain", subtitle_style),
            Paragraph("Mise à jour: 10/08/2026", ParagraphStyle('RightH2', parent=subtitle_style, alignment=2))
        ]
    ]

    header_table = Table(header_data, colWidths=[21.0*cm, 7.1*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_HEADER),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))

    story.append(header_table)
    story.append(Spacer(1, 0.2*cm))

    data = [
        [
            Paragraph("Établissement & Contact", header_cell),
            Paragraph("Adresse Postale Complète", header_cell),
            Paragraph("Téléphones Directs", header_cell),
            Paragraph("Email & Site Web", header_cell),
            Paragraph("Statut Prospection", header_cell),
            Paragraph("Notes Réelles de Suivi & Commentaires", header_cell)
        ]
    ]

    venues = [
        {
            "name": "Domaine de la Durantie",
            "type": "Hébergement Groupe & Domaine Luxe",
            "contact": "Gérance Durantie",
            "addr": "La Durantie, 401-405 Grande Route de Grésigne, 81140 Castelnau-de-Montmiral",
            "phone": "06 43 02 79 64\n05 63 33 21 00",
            "email": "reservations@durantie.com",
            "status": "[  ] À contacter",
            "notes": "Domaine de luxe groupe. Proposer audit parcours hébergement."
        },
        {
            "name": "Château Tauziès",
            "type": "Château Viticole & Séminaires",
            "contact": "Direction Tauziès",
            "addr": "1850 Route de Cordes, 81600 Gaillac",
            "phone": "05 63 41 26 80",
            "email": "contact@chateaudetauzies.com",
            "status": "[  ] À contacter",
            "notes": "Vignoble et séminaires d'entreprise de prestige."
        },
        {
            "name": "Moulin de Trusse",
            "type": "Chambre d'Hôtes & Moulin",
            "contact": "Baptiste M.",
            "addr": "1485 Route du Moulin de Trusse, 81630 La Sauzière-Saint-Jean",
            "phone": "06 37 93 99 42",
            "email": "baptistempage@gmail.com",
            "status": "[  ] À contacter",
            "notes": "Moulin restauré au bord de l'eau. Contact direct Baptiste."
        },
        {
            "name": "La Maison de Clément",
            "type": "Gîte de Charme",
            "contact": "Gîtes de France Tarn",
            "addr": "302 Chemin Toulze – Les Fortis, 81310 Lisle-sur-Tarn",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter",
            "notes": "Gîte pittoresque."
        },
        {
            "name": "La Maison de Romain",
            "type": "Gîte d'Exception",
            "contact": "Gîtes de France Tarn",
            "addr": "Lieu-dit Lourate, 81140 Puycelsi",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter",
            "notes": "Maison de village haut de gamme."
        },
        {
            "name": "Ma vie là ! Au bord de l'eau",
            "type": "Gîte de Charme au Bord de l'Eau",
            "contact": "Gîtes de France Tarn",
            "addr": "22 Rue du Quai, 81600 Gaillac",
            "phone": "05 63 48 83 01",
            "email": "reservation@gites-tarn.com",
            "status": "[  ] À contacter",
            "notes": "Cadre naturel rivière."
        },
        {
            "name": "Hôtel Particulier Delga",
            "type": "Hôtel Particulier & Maison d'Hôtes",
            "contact": "Propriétaires Delga",
            "addr": "28 Rue des Frères Delga, 81600 Gaillac",
            "phone": "06 36 80 01 01",
            "email": "hoteldelga@gmail.com",
            "status": "[  ] À contacter",
            "notes": "Demeure historique centre-ville."
        },
        {
            "name": "Hôtel La Grande Roche",
            "type": "Hôtel & Domaine Lécusse",
            "contact": "Réception Lécusse",
            "addr": "105 Impasse Puech Aymond D 922, 81600 Broze",
            "phone": "06 79 82 80 87",
            "email": "reception@chateaulecusse.fr",
            "status": "[  ] À contacter",
            "notes": "Domaine hôtelier de caractère."
        },
        {
            "name": "Hôtel du Château de Salettes",
            "type": "Hôtel 4* & Resto Gastronomique",
            "contact": "Direction Générale",
            "addr": "Lieu-dit Salettes, 81140 Cahuzac-sur-Vère",
            "phone": "05 63 33 60 60",
            "email": "salettes@chateaudesalettes.com",
            "status": "[  ] À contacter",
            "notes": "Château 4* luxe & restaurant gastronomique au cœur des vignes."
        },
        {
            "name": "Appartement L'Étoile de Mer",
            "type": "Location de Vacances Bord de Mer",
            "contact": "GISÈNE (Contact Direct)",
            "addr": "Quai de la Résistance, 34200 Sète",
            "phone": "06 15 41 84 20",
            "email": "contact@location-sete.site",
            "status": "[  ] À contacter",
            "notes": "Contact direct : Gisène. Appartement vue mer à Sète."
        },
        {
            "name": "La Terrasse du Mont-Blanc",
            "type": "Chalet Prestige & Événementiel",
            "contact": "DAVID (Contact sur place)",
            "addr": "1250 Route de la Combe, 74700 Cordon",
            "phone": "04 65 84 56 02 (Fixe)\n06 35 86 92 97 (Mobile)",
            "email": "contact@terrassedumontblanc.com",
            "status": "[X] 1er Appel fait / Relance",
            "notes": "Contact sur place : David. Chalet d'exception & mariages / séminaires. A dit oui mais sans nouvelle."
        }
    ]

    for v in venues:
        name_cell = Paragraph(f"<b>{v['name']}</b><br/><font color='#6B21A8'><b>Contact: {v['contact']}</b></font><br/><font color='#64748B'>{v['type']}</font>", cell_name)
        addr_cell = Paragraph(v['addr'], cell_addr)
        phone_cell = Paragraph(v['phone'].replace('\n', '<br/>'), cell_phone)
        email_cell = Paragraph(v['email'].replace('\n', '<br/>'), cell_email)
        status_cell = Paragraph(v['status'].replace('\n', '<br/>'), cell_status)
        notes_cell = Paragraph(f"<font color='#0F172A'><b>{v['notes']}</b></font>", cell_notes)

        data.append([name_cell, addr_cell, phone_cell, email_cell, status_cell, notes_cell])

    col_widths = [5.5*cm, 5.8*cm, 3.5*cm, 4.5*cm, 3.0*cm, 5.8*cm]
    
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
    print(f"✅ PDF Prospection généré avec succès : {pdf_path}")
    print(f"✅ Copie Desktop disponible : {desktop_pdf}")

if __name__ == "__main__":
    generate_pdf()
