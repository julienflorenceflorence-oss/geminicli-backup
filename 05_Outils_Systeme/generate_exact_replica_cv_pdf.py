# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, '/Users/admin/Library/Python/3.9/lib/python/site-packages')
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

class PrecisionCleanCVPDF:
    def __init__(self, filename):
        self.filename = filename
        self.c = canvas.Canvas(filename, pagesize=A4)
        self.width, self.height = A4 # 210mm x 297mm (1 Page A4 Strict)

    def draw_cv(self):
        c = self.c
        
        # Colors
        bg_main = colors.HexColor("#0B0C10")
        bg_sidebar = colors.HexColor("#13161F")
        gold_primary = colors.HexColor("#D4AF37")
        gold_bright = colors.HexColor("#FACC15")
        text_white = colors.HexColor("#F8FAFC")
        text_gray = colors.HexColor("#E2E8F0")
        text_muted = colors.HexColor("#94A3B8")
        btn_dark_bg = colors.HexColor("#161A25")
        btn_border_muted = colors.HexColor("#3C4150")
        pill_bg = colors.HexColor("#141822")
        
        # 1. Main Background
        c.setFillColor(bg_main)
        c.rect(0, 0, self.width, self.height, fill=1, stroke=0)
        
        # 2. Sidebar Background (width 68mm)
        c.setFillColor(bg_sidebar)
        c.rect(0, 0, 68*mm, self.height, fill=1, stroke=0)
        
        # 3. Vertical Gold Line Divider
        c.setStrokeColor(gold_primary)
        c.setLineWidth(0.8)
        c.line(68*mm, 0, 68*mm, self.height)
        
        # --------------------------------------------------------
        # SIDEBAR CONTENT (Left Column, x=0 to 68mm)
        # --------------------------------------------------------
        
        # Profile Photo (x=14mm, y=238mm, w=40mm, h=46mm)
        photo_path = "Projets/prospection job/jost-hotel-bordeaux/04_Livrables/Images/julien_florence_photo.png"
        if not os.path.exists(photo_path):
            photo_path = "/tmp/extracted_photo_0.png"
            
        if os.path.exists(photo_path):
            c.drawImage(photo_path, 14*mm, 238*mm, width=40*mm, height=46*mm, preserveAspectRatio=True, mask='auto')
            c.setStrokeColor(gold_primary)
            c.setLineWidth(1.2)
            c.roundRect(14*mm, 238*mm, 40*mm, 46*mm, radius=3*mm, stroke=1, fill=0)
            
        # 4 Action Buttons with Rounded Corners (roundRect) + PDF Hyperlinks
        buttons = [
            ("tel:0661747573", "06 61 74 75 73", False, False),
            ("mailto:julienflorence.florence@gmail.com", "EMAIL", False, False),
            ("https://linkedin.com/in/alban-ruggiero/", "AGENDA", True, False),
            ("https://github.com/julienflorenceflorence-oss/geminicli-backup/tree/main/Projets/prospection%20job/jost-hotel-bordeaux/04_Livrables/PDF", "ACCES CV INTERACTIF", False, True)
        ]
        
        btn_y = 224*mm
        for url, text, is_gold_filled, is_gold_border in buttons:
            if is_gold_filled:
                c.setFillColor(gold_bright)
                c.setStrokeColor(gold_bright)
                c.roundRect(9*mm, btn_y, 50*mm, 7.5*mm, radius=3.75*mm, stroke=1, fill=1)
                c.setFillColor(colors.HexColor("#0B0C10"))
                c.setFont("Helvetica-Bold", 7.8)
            else:
                c.setFillColor(btn_dark_bg)
                c.setStrokeColor(gold_primary if is_gold_border else btn_border_muted)
                c.setLineWidth(0.8)
                c.roundRect(9*mm, btn_y, 50*mm, 7.5*mm, radius=3.75*mm, stroke=1, fill=1)
                c.setFillColor(text_white)
                c.setFont("Helvetica-Bold", 7.2)
                
            c.drawCentredString(34*mm, btn_y + 2.4*mm, text)
            c.linkURL(url, (9*mm, btn_y, 59*mm, btn_y + 7.5*mm), relative=0)
            btn_y -= 9.2*mm

        # Sidebar Sections
        sidebar_sections = [
            ("EXPERTISES METSIER", [
                "Evenementiel de Prestige & MICE",
                "Hospitalite & Codes du Luxe (LHW)",
                "Developpement B2B & Acquisition",
                "Management d'equipes (3-20 ETP)",
                "Pilotage Commercial (CA, P&L, Marge)",
                "Sommellerie de Prestige & Gastronomie"
            ]),
            ("SOFT SKILLS", [
                "ENTJ-A | 94% Rationnel & Organise",
                "Sens du service client d'exception",
                "Aisance relationnelle client VIP",
                "Leadership federateur & Terrain",
                "Esprit d'entreprise & Resilience"
            ]),
            ("LANGUES", [
                "Anglais : Usage pro (C1, 2 ans UK/IRL)",
                "Neerlandais : B2"
            ]),
            ("FORMATION", [
                "Bachelor Marketing & Commerce (2025)",
                "HTML5 & CSS3 - Google Academy"
            ])
        ]
        
        sec_y = 182*mm
        for title, items in sidebar_sections:
            c.setFillColor(gold_primary)
            c.setFont("Times-Bold", 9)
            c.drawString(9*mm, sec_y, title)
            
            c.setStrokeColor(gold_primary)
            c.setLineWidth(0.5)
            c.line(9*mm, sec_y - 1.5*mm, 59*mm, sec_y - 1.5*mm)
            
            sec_y -= 5.5*mm
            c.setFillColor(text_gray)
            c.setFont("Helvetica", 7)
            
            for item in items:
                c.setFillColor(gold_primary)
                c.drawString(9*mm, sec_y, ">")
                c.setFillColor(text_gray)
                c.drawString(12*mm, sec_y, item)
                sec_y -= 4*mm
                
            sec_y -= 2*mm

        c.setFillColor(gold_primary)
        c.setFont("Helvetica-Oblique", 6)
        c.drawCentredString(34*mm, 7*mm, "CV complet & diplomes accessibles en 1 clic")

        # --------------------------------------------------------
        # MAIN CONTENT (Right Column, x=74mm to 200mm)
        # --------------------------------------------------------
        
        # Header Name
        c.setFillColor(gold_primary)
        c.setFont("Times-Bold", 23)
        c.drawString(74*mm, 280*mm, "JULIEN FLORENCE")
        
        # Subtitle (Exact Command)
        c.setFillColor(text_white)
        c.setFont("Helvetica-Bold", 9.2)
        c.drawString(74*mm, 272*mm, "| DIRECTEUR D'HOTEL HYBRIDE")
        
        # Presentation Text (Clean, Spaced)
        summary_text = "Directeur d'Hotel Hybride fort de 25 ans d'experience combinant la rigueur operationnelle et l'excellence du service de prestige (Palaces 5* & etoiles) au pilotage de centres de profit, Revenue Management et virage MICE B2B. Expert de l'evenementiel et du F&B, je suis immediatement operationnel sur Bordeaux pour piloter le site JOST Gare Saint-Jean."
        
        c.setFillColor(text_gray)
        c.setFont("Helvetica", 7.6)
        
        words = summary_text.split()
        line = ""
        summary_y = 265*mm
        for w in words:
            if c.stringWidth(line + " " + w, "Helvetica", 7.6) < 125*mm:
                line += (" " if line else "") + w
            else:
                c.drawString(74*mm, summary_y, line)
                summary_y -= 3.6*mm
                line = w
        if line:
            c.drawString(74*mm, summary_y, line)
            summary_y -= 3.6*mm
            
        # Section Title: EXPERIENCES PROFESSIONNELLES
        exp_y = summary_y - 3*mm
        c.setFillColor(gold_primary)
        c.setFont("Times-Bold", 10.5)
        c.drawString(74*mm, exp_y, "EXPERIENCES PROFESSIONNELLES")
        
        title_width = c.stringWidth("EXPERIENCES PROFESSIONNELLES", "Times-Bold", 10.5)
        c.setStrokeColor(gold_primary)
        c.setLineWidth(0.6)
        c.line(74*mm + title_width + 3*mm, exp_y + 1.2*mm, 200*mm, exp_y + 1.2*mm)
        
        # 5 Jobs with Perfect Spacing between entries
        jobs = [
            ("Responsable Commercial & Acquisition Tech", "2025 - PRESENT", "HAPPY HOUSE | ACQUISITION & RENTABILITE B2B", [
                "Coaching et pilotage d'une equipe de 3 collaborateurs (objectifs de conquete, animation).",
                "Integration d'outils d'acquisition digitaux (CRM, prospection multi-canal) et suivi des KPIs.",
                "Definition de la strategie commerciale Go-To-Market et optimisation des marges."
            ], ["Management", "CRM", "KPIs", "B2B"]),
            
            ("Responsable de Division HRE (Hotellerie, Restauration & Evenementiel)", "2022 - 2024", "RAS INTERIM | SERVICE & EVENEMENTIEL - CA DIVISION 2.6 M EUR", [
                "Developpement B2B & Comptes Cles : Gestion de 20 clients corporate (hotels, traiteurs de prestige).",
                "Management operationnel de 20 ETP par semaine (recrutement, plannings, formation personnel).",
                "Garant de la conformite reglementaire, de la gestion du P&L divisionnaire et de la fidelisation client."
            ], ["Hotellerie-Restauration", "Evenementiel B2B", "Management ETP"]),
            
            ("Negociateur Immobilier & Manager Leader", "2015 - 2021", "CENTURY 21 (Paris) & CABINET BEDIN (Toulouse)", [
                "Negociation commerciale et pilotage d'un portefeuille de clients exigeants (120k EUR CA moyen personnel).",
                "Recrutement, formation, animation et coaching de 5 negociateurs sur le terrain et en agence.",
                "Animation d'actions commerciales de terrain et developpement de partenariats locaux."
            ], ["Negociation Haut de Gamme", "Coaching Sales", "Reseau Local"]),
            
            ("Directeur de Restaurant & Partenaire Evenementiel", "2010 - 2015", "MA SALLE A MANGER | PARIS 1er (PLACE DAUPHINE)", [
                "Duplication des standards de l'hotellerie de luxe pour piloter le restaurant (15 salaries, P&L) : croissance de +140% du CA en 5 ans (passage de 250 k EUR a 600 k EUR).",
                "Evenementiel culturel & Corporate : Partenaire gastronomique exclusif de la Galerie Nabokof (Paris 1er) pour vernissages ; accueil de clubs d'affaires et EVG de prestige."
            ], ["Evenementiel Culturel", "Clubs d'Affaires", "Rentabilite (+140% CA)"]),
            
            ("Service de Prestige & Gestion Clienteles VIP", "2000 - 2009", "PALACES 5* (LHW), YACHTING DE LUXE & SOMMELLERIE ETOILEE | IRLANDE, ST-BARTH, ANGLETERRE", [
                "1er Sommelier (2003-2004) : Westbury Palace 5* Dublin (Sommelier de M. Bono - U2). Management de 20 personnes.",
                "Chef Barman (2001-2002) : Le Clos 1* Michelin (Bath, Angleterre). Creation de cartes cocktails (CA : 6 M EUR).",
                "Adjoint Room Service (2000-2001) : Guanahani Palace 5* St-Barth. Service Nouvel An yachts de luxe & VIPs."
            ], ["Standards Palaces (LHW)", "Clienteles VIP", "Sommellerie & Bar"])
        ]
        
        curr_y = exp_y - 6*mm
        for role, dates, company, bullets, tags in jobs:
            # Role Title
            c.setFillColor(gold_primary)
            c.setFont("Helvetica-Bold", 8.2)
            c.drawString(74*mm, curr_y, role)
            
            # Dates
            c.setFillColor(text_muted)
            c.setFont("Helvetica-Bold", 7.2)
            c.drawRightString(200*mm, curr_y, dates)
            
            # Company
            curr_y -= 3.5*mm
            c.setFillColor(text_white)
            c.setFont("Helvetica-Bold", 7)
            c.drawString(74*mm, curr_y, company)
            
            # Bullets
            curr_y -= 3.2*mm
            c.setFillColor(text_gray)
            c.setFont("Helvetica", 6.5)
            
            for b in bullets:
                b_words = b.split()
                b_line = "•"
                for bw in b_words:
                    if c.stringWidth(b_line + " " + bw, "Helvetica", 6.5) < 124*mm:
                        b_line += (" " if b_line != "•" else " ") + bw
                    else:
                        c.drawString(74*mm, curr_y, b_line)
                        curr_y -= 2.8*mm
                        b_line = "  " + bw
                if b_line:
                    c.drawString(74*mm, curr_y, b_line)
                    curr_y -= 2.8*mm
                    
            # Tag Pills (Exact rounded pills with clear bottom margin)
            curr_y -= 0.2*mm
            c.setFillColor(pill_bg)
            c.setStrokeColor(gold_primary)
            c.setLineWidth(0.4)
            c.setFont("Helvetica", 5.8)
            
            tag_x = 74*mm
            for tag in tags:
                tag_str = f"({tag})"
                tw = c.stringWidth(tag_str, "Helvetica", 5.8) + 3*mm
                if tag_x + tw > 200*mm:
                    curr_y -= 3.5*mm
                    tag_x = 74*mm
                c.roundRect(tag_x, curr_y, tw, 3.2*mm, radius=1.6*mm, fill=1, stroke=1)
                c.setFillColor(gold_primary)
                c.drawCentredString(tag_x + tw/2.0, curr_y + 0.8*mm, tag_str)
                c.setFillColor(pill_bg)
                tag_x += tw + 1.5*mm
                
            # Generous spacing between end of this job and start of next job
            curr_y -= 4.2*mm

        c.save()
        print(f"✅ PDF Calibré avec Fins d'Expériences Nettes généré : {self.filename}")

def build_all_clean_pdfs():
    out_file = "Projets/prospection job/jost-hotel-bordeaux/04_Livrables/PDF/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.pdf"
    desktop_jost = '/Users/admin/Desktop/JOST/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.pdf'
    desktop_root = '/Users/admin/Desktop/CV_Julien_Florence_JOST_Bordeaux.pdf'
    
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    os.makedirs(os.path.dirname(desktop_jost), exist_ok=True)
    
    for path in [out_file, desktop_jost, desktop_root]:
        builder = PrecisionCleanCVPDF(path)
        builder.draw_cv()

if __name__ == "__main__":
    build_all_clean_pdfs()
