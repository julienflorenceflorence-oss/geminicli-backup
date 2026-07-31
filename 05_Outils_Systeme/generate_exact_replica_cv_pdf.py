# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, '/Users/admin/Library/Python/3.9/lib/python/site-packages')
from fpdf import FPDF

class ExactReplicaCVPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=False)
        self.set_margins(0, 0, 0)
        
    def draw_layout(self):
        # 1. Main Background (#0B0C10)
        self.set_fill_color(11, 12, 16)
        self.rect(0, 0, 210, 297, 'F')
        
        # 2. Sidebar Background (#13161F)
        self.set_fill_color(19, 22, 31)
        self.rect(0, 0, 68, 297, 'F')
        
        # 3. Sidebar Divider Line (#D4AF37)
        self.set_draw_color(212, 175, 55)
        self.set_line_width(0.3)
        self.line(68, 0, 68, 297)

def clean_txt(text):
    for emoji in ["📞", "✉️", "📍", "🔗", "🏆", "📌", "😊", "🧐", "⚡", "🎯", "🤾", "✨", "📜", "📊", "💰", "💼", "🏢", "👤", "⚙️", "🎙️", "📩", "🤝", "🛏️", "🍽️", "🍸", "🚀", "🧠", "🏛️", "📐", "💬"]:
        text = text.replace(emoji, "")
    return text.replace("—", "-").replace("’", "'").replace("°", "o").replace("€", "EUR").replace("…", "...").replace("«", '"').replace("»", '"').replace("œ", "oe").replace("Œ", "OE")

def generate_pdf(out_path):
    pdf = ExactReplicaCVPDF()
    pdf.add_page()
    pdf.draw_layout()
    
    # ----------------------------------------------------
    # SIDEBAR CONTENT (Left Column, width 68mm)
    # ----------------------------------------------------
    
    # Profile Photo (Top Left)
    photo_path = "/Users/admin/.gemini/antigravity/brain/3b3f54ca-b09a-4ea4-9dc8-59a0af5a76aa/.user_uploaded/media__1785320733290.png"
    if os.path.exists(photo_path):
        pdf.image(photo_path, x=14, y=10, w=40, h=46)
        pdf.set_draw_color(212, 175, 55)
        pdf.set_line_width(0.5)
        pdf.rect(14, 10, 40, 46, 'D')
    
    # 4 Action Buttons
    buttons = [
        ("06 61 74 75 73", False, False),
        ("EMAIL", False, False),
        ("AGENDA", True, False),
        ("ACCES CV INTERACTIF", False, True)
    ]
    
    btn_y = 60
    for text, is_yellow, is_border_gold in buttons:
        if is_yellow:
            pdf.set_fill_color(234, 179, 8)
            pdf.set_draw_color(234, 179, 8)
            pdf.set_text_color(11, 12, 16)
        else:
            pdf.set_fill_color(22, 26, 37)
            pdf.set_draw_color(212, 175, 55) if is_border_gold else pdf.set_draw_color(60, 65, 80)
            pdf.set_text_color(248, 250, 252)
            
        pdf.set_font('Helvetica', 'B', 7)
        pdf.rect(9, btn_y, 50, 6.5, 'DF')
        pdf.set_xy(9, btn_y + 1.2)
        pdf.cell(50, 4, clean_txt(text), align='C')
        btn_y += 8.5
        
    # Sidebar Sections
    sidebar_sections = [
        ("EXPERTISES METSIER", [
            "Evenementiel de Prestige & MICE",
            "Hospitalite & Codes du Luxe (LHW)",
            "Developpement B2B & Acquisition",
            "Management d'equipes (3-20 ETP)",
            "Pilotage Commercial (CA, P&L, Marge)",
            "Sommellerie de Prestige & Gastronomie",
            "Revenue Management & Doyield JOST"
        ]),
        ("SOFT SKILLS", [
            "ENTJ-A | 94% Rationnel & Organise",
            "Sens du service client d'exception",
            "Aisance relationnelle clienteles VIP",
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
    
    sec_y = 98
    for title, items in sidebar_sections:
        pdf.set_xy(9, sec_y)
        pdf.set_font('Times', 'B', 9)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(50, 4, clean_txt(title))
        
        pdf.set_draw_color(212, 175, 55)
        pdf.set_line_width(0.2)
        pdf.line(9, sec_y + 4.5, 59, sec_y + 4.5)
        
        sec_y += 6.5
        pdf.set_font('Helvetica', '', 6.8)
        pdf.set_text_color(203, 213, 225)
        
        for item in items:
            pdf.set_xy(9, sec_y)
            pdf.cell(3, 3.5, ">", align='L')
            pdf.set_xy(12, sec_y)
            pdf.multi_cell(47, 3.5, clean_txt(item))
            sec_y = pdf.get_y() + 0.5
            
        sec_y += 2.5
        
    # ----------------------------------------------------
    # MAIN CONTENT (Right Column, x=74mm to 200mm)
    # ----------------------------------------------------
    
    # Header Name
    pdf.set_xy(74, 10)
    pdf.set_font('Times', 'B', 22)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(126, 8, clean_txt("JULIEN FLORENCE"))
    
    # Subtitle (UPDATED TO DIRECTEUR D'HÔTEL HYBRIDE — JOST BORDEAUX)
    pdf.set_xy(74, 18)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(248, 250, 252)
    pdf.cell(126, 5, clean_txt("| DIRECTEUR D'HÔTEL HYBRIDE — JOST BORDEAUX"))
    
    # Profile Summary Paragraph
    pdf.set_xy(74, 25)
    pdf.set_font('Helvetica', '', 7.2)
    pdf.set_text_color(226, 232, 240)
    summary = "Directeur d'Hotel Hybride & Manager fort de 15 ans d'experience combinant la rigueur operationnelle et l'excellence du service de prestige (Palaces 5* & etoiles) au pilotage de centres de profit, Revenue Management (Doyield) et virage MICE B2B. Expert de l'evenementiel haut de gamme et du F&B, je suis immediatement mobile et operationnel pour piloter le site JOST Bordeaux Gare Saint-Jean."
    pdf.multi_cell(126, 3.4, clean_txt(summary))
    
    # Section Title: EXPERIENCES PROFESSIONNELLES
    curr_y = pdf.get_y() + 3
    pdf.set_xy(74, curr_y)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(65, 5, clean_txt("EXPERIENCES PROFESSIONNELLES"))
    
    # Gold horizontal rule
    pdf.set_draw_color(212, 175, 55)
    pdf.set_line_width(0.3)
    pdf.line(139, curr_y + 3, 200, curr_y + 3)
    
    curr_y += 7
    
    # Experiences List (Exact text from attached image, with JOST Directorship adaptation for Job 1)
    jobs = [
        ("Directeur d'Hotel Hybride & Developpement Commercial", "2025 - PRESENT", "HAPPY HOUSE | ACQUISITION & RENTABILITE B2B - CIBLE JOST BORDEAUX", [
            "Coaching et pilotage d'une equipe de 3 collaborateurs (objectifs de conquete MICE B2B, animation).",
            "Integration de la solution Doyield pour le Yield Management hybride (dortoirs vs chambres Signature).",
            "Definition de la strategie commerciale Go-To-Market et privatisation du Lieu Cheri et du Rooftop."
        ], ["Management", "Doyield", "KPIs", "MICE B2B", "JOST Bordeaux"]),
        
        ("Responsable de Division HRE (Hotellerie, Restauration & Evenementiel)", "2022 - 2024", "RAS INTERIM | SERVICE & EVENEMENTIEL - CA DIVISION 2.6 M EUR", [
            "Developpement B2B & Comptes Cles : Gestion de 20 clients corporate (hotels, traiteurs de prestige).",
            "Management operationnel de 20 ETP par semaine (recrutement, plannings, formation personnel).",
            "Garant de la conformite reglementaire, de la gestion du P&L divisionnaire et de la fidelisation client."
        ], ["Hotellerie-Restauration", "Evenementiel B2B", "Management ETP"]),
        
        ("Negociateur Immobilier & Manager Leader", "2015 - 2021", "CENTURY 21 (Paris) & CABINET BEDIN (Toulouse)", [
            "Negociation commerciale et pilotage d'un portefeuille de clients exigeants (120k EUR CA annuel personnel).",
            "Recrutement, formation, animation et coaching de 5 negociateurs sur le terrain et en agence.",
            "Animation d'actions commerciales de terrain et developpement de partenariats locaux."
        ], ["Negociation Haut de Gamme", "Coaching Sales", "Reseau Local"]),
        
        ("Directeur de Restaurant & Partenaire Evenementiel", "2010 - 2015", "MA SALLE A MANGER | PARIS 1er (PLACE DAUPHINE)", [
            "Duplication des standards de l'hotellerie de luxe pour piloter le restaurant (15 salaries, P&L) : croissance de +140% du CA en 5 ans (passage de 250 k EUR a 600 k EUR).",
            "Evenementiel culturel & Corporate : Partenaire gastronomique exclusif de la Galerie Nabokof (Paris 1er) pour vernissages ; accueil de clubs d'affaires et EVG de prestige."
        ], ["Evenementiel Culturel", "Clubs d'Affaires", "Rentabilite (+140% CA)"]),
        
        ("Service de Prestige & Gestion Clienteles VIP", "2000 - 2009", "PALACES 5* (LHW), YACHTING DE LUXE & SOMMELLERIE ETOILEE | IRLANDE, ST-BARTH, ANGLETERRE", [
            "1er Sommelier (2003-2004) : The Westbury (Palace 5*, Dublin, 1* Michelin). Sommelier privilegie de M. Bono (U2) lors de receptions privees. Management de 20 personnes.",
            "Chef Barman (2001-2002) : Le Clos (1* Michelin, Bath, Angleterre). Creation de la carte des cocktails, management des barmans, gestion des stocks et de la clientele (CA : 6 M EUR).",
            "Adjoint du Responsable Room Service (2000-2001) : The Guanahani (Palace 5*, St-Barth). Supervision de 20 personnes. Service pour le Nouvel An sur les yachts de luxe et personnalites VIP."
        ], ["Standards Palaces (LHW)", "Clienteles VIP", "Sommellerie & Bar"])
    ]
    
    for role, dates, company, bullets, tags in jobs:
        # Job Role + Dates
        pdf.set_xy(74, curr_y)
        pdf.set_font('Helvetica', 'B', 8.2)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(85, 4, clean_txt(role), align='L')
        
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(148, 163, 184)
        pdf.cell(41, 4, clean_txt(dates), align='R')
        
        # Company
        curr_y += 4
        pdf.set_xy(74, curr_y)
        pdf.set_font('Helvetica', 'B', 7.2)
        pdf.set_text_color(248, 250, 252)
        pdf.cell(126, 3.6, clean_txt(company))
        
        # Bullets
        curr_y += 3.8
        pdf.set_font('Helvetica', '', 6.8)
        pdf.set_text_color(203, 213, 225)
        for bullet in bullets:
            pdf.set_xy(74, curr_y)
            pdf.cell(3, 3, "-", align='L')
            pdf.set_xy(77, curr_y)
            pdf.multi_cell(123, 3, clean_txt(bullet))
            curr_y = pdf.get_y()
            
        # Tags (Pill Badges)
        curr_y += 0.8
        pdf.set_xy(74, curr_y)
        pdf.set_font('Helvetica', '', 6)
        pdf.set_text_color(212, 175, 55)
        pdf.set_draw_color(212, 175, 55)
        pdf.set_fill_color(20, 24, 34)
        
        tag_x = 74
        for tag in tags:
            tag_txt = clean_txt(f"({tag})")
            t_w = pdf.get_string_width(tag_txt) + 3.5
            if tag_x + t_w > 200:
                curr_y += 4
                tag_x = 74
            pdf.rect(tag_x, curr_y, t_w, 3.6, 'DF')
            pdf.set_xy(tag_x, curr_y + 0.3)
            pdf.cell(t_w, 2.8, tag_txt, align='C')
            tag_x += t_w + 1.8
            
        curr_y += 5

    pdf.output(out_path)
    print(f"✅ PDF Réplique 100% Conforme Image + JOST Title généré : {out_path}")

if __name__ == "__main__":
    out_file = "Projets/prospection job/jost-hotel-bordeaux/04_Livrables/PDF/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.pdf"
    generate_pdf(out_file)
