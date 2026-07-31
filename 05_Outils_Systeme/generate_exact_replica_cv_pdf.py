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
            "Management Retail & Vente (3-20 collab.)",
            "Pilotage Commercial & KPIs (CA, P&L)",
            "Gestion des Flux, Appro. & Stocks",
            "Excellence Client & Fidelisation",
            "CRM Expert & Smarketing (Bitrix24)",
            "Virage MICE & Revenue Mgt Doyield"
        ]),
        ("SOFT SKILLS", [
            "ENTJ-A | 94% Rationnel & Organise",
            "Sens aigu de l'organisation & Rigueur",
            "Leadership federateur (Posture Girafe)",
            "Gestion de conflits & Resolution de prob.",
            "Management participatif & Terrain"
        ]),
        ("LANGUES", [
            "Anglais : Courant (B2)",
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
            
        sec_y += 3
        
    # ----------------------------------------------------
    # MAIN CONTENT (Right Column, x=74mm to 200mm)
    # ----------------------------------------------------
    
    # Header Name
    pdf.set_xy(74, 12)
    pdf.set_font('Times', 'B', 22)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(126, 8, clean_txt("JULIEN FLORENCE"))
    
    # Subtitle
    pdf.set_xy(74, 20)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(248, 250, 252)
    pdf.cell(126, 5, clean_txt("| MANAGER COMMERCIAL & OPERATIONNEL — JOST BORDEAUX"))
    
    # Profile Summary Paragraph
    pdf.set_xy(74, 27)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    summary = "Manager commercial et operationnel avec 15 ans d'experience dans l'animation d'equipes et la gestion de centres de profit (jusqu'a 2.6 M EUR). Alliant la rigueur operationnelle issue de l'hotellerie de luxe (Palaces 5* & Etoiles) a de solides competences en techniques de vente et outils technologiques (Bachelor Marketing, CRM, Revenue Management Doyield), je suis oriente terrain et satisfaction client. Immediatement mobile et operationnel sur Bordeaux pour dynamiser la performance de votre point de vente."
    pdf.multi_cell(126, 3.6, clean_txt(summary))
    
    # Section Title: EXPERIENCES PROFESSIONNELLES
    curr_y = pdf.get_y() + 4
    pdf.set_xy(74, curr_y)
    pdf.set_font('Times', 'B', 11)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(65, 5, clean_txt("EXPERIENCES PROFESSIONNELLES"))
    
    # Gold horizontal rule
    pdf.set_draw_color(212, 175, 55)
    pdf.set_line_width(0.3)
    pdf.line(139, curr_y + 3, 200, curr_y + 3)
    
    curr_y += 8
    
    # Experiences List (Exact 5 jobs from screenshot)
    jobs = [
        ("Responsable Developpement Commercial", "2025 - PRESENT", "HAPPY HOUSE | SOLUTIONS B2B & RENTABILITE", [
            "Management et coaching d'une equipe de 3 collaborateurs (animation, objectifs).",
            "Integration d'outils d'acquisition Tech, automatisation et suivi des KPIs de performance.",
            "Contribution directe aux projets transverses et a l'evolution des processus de vente."
        ], ["Management", "Processus", "KPIs"]),
        
        ("Gestionnaire de Centre de Profit & Manager", "2022 - 2024", "RAS INTERIM | LOGISTIQUE & SERVICES - CA 2.6 M EUR", [
            "Management quotidien de 20 ETP par semaine (formation, plannings, evaluations).",
            "Pilotage commercial : analyse des indicateurs cles et gestion de 25 comptes B2B strategiques.",
            "Garant du respect strict des procedures internes et de la conformite reglementaire."
        ], ["Gestion d'equipe", "Indicateurs", "Procedures"]),
        
        ("Conseiller Leader - Expert Immobilier", "2015 - 2021", "CENTURY 21 (Paris) & CABINET BEDIN (Toulouse) - CA global 7 M EUR", [
            "Negociation commerciale et pilotage d'un portefeuille clients exigeants (120k EUR CA personnel).",
            "Fidelisation d'une clientele locale et animation d'actions commerciales de terrain.",
            "Grand sens de l'organisation et rigueur administrative dans le suivi des dossiers de vente."
        ], ["Negociation", "Rigueur", "Fidelisation"]),
        
        ("Directeur de Restaurant", "2010 - 2015", "MA SALLE A MANGER | PARIS 1er", [
            "Animation quotidienne de l'espace de vente et management d'une equipe de 15 salaries.",
            "Pilotage de la rentabilite (comptes d'exploitation, P&L) : croissance de +140% du CA.",
            "Gestion rigoureuse des stocks, approvisionnements et respect strict des normes de securite."
        ], ["Gestion de stock", "P&L", "Animation"]),
        
        ("Management & Service d'Excellence", "2000 - 2009", "PALACES 5* & RESTAURANTS ETOILES | DUBLIN, SAINT-BARTH, ANGLETERRE", [
            "Management operationnel d'equipes de 7 a 20 collaborateurs sous haute exigence (Room Service Palace Guanahani 5* St-Barth, Au Clos Angleterre).",
            "Fidelisation d'une clientele internationale selon les standards prestigieux LHW.",
            "Capacites de resolution de problemes et de gestion des conflits en situation de forte affluence."
        ], ["Excellence", "Resolution de problemes"])
    ]
    
    for role, dates, company, bullets, tags in jobs:
        # Job Role + Dates
        pdf.set_xy(74, curr_y)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(85, 4, clean_txt(role), align='L')
        
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(148, 163, 184)
        pdf.cell(41, 4, clean_txt(dates), align='R')
        
        # Company
        curr_y += 4.2
        pdf.set_xy(74, curr_y)
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(248, 250, 252)
        pdf.cell(126, 3.8, clean_txt(company))
        
        # Bullets
        curr_y += 4
        pdf.set_font('Helvetica', '', 7)
        pdf.set_text_color(203, 213, 225)
        for bullet in bullets:
            pdf.set_xy(74, curr_y)
            pdf.cell(3, 3.2, "-", align='L')
            pdf.set_xy(77, curr_y)
            pdf.multi_cell(123, 3.2, clean_txt(bullet))
            curr_y = pdf.get_y()
            
        # Tags (Pill Badges)
        curr_y += 1
        pdf.set_xy(74, curr_y)
        pdf.set_font('Helvetica', '', 6.2)
        pdf.set_text_color(212, 175, 55)
        pdf.set_draw_color(212, 175, 55)
        pdf.set_fill_color(20, 24, 34)
        
        tag_x = 74
        for tag in tags:
            tag_txt = clean_txt(f"({tag})")
            t_w = pdf.get_string_width(tag_txt) + 4
            if tag_x + t_w > 200:
                curr_y += 4.5
                tag_x = 74
            pdf.rect(tag_x, curr_y, t_w, 3.8, 'DF')
            pdf.set_xy(tag_x, curr_y + 0.4)
            pdf.cell(t_w, 3, tag_txt, align='C')
            tag_x += t_w + 2
            
        curr_y += 5.5

    pdf.output(out_path)
    print(f"✅ PDF Réplique Exacte (5 postes originaux) généré : {out_path}")

if __name__ == "__main__":
    out_file = "Projets/prospection job/jost-hotel-bordeaux/04_Livrables/PDF/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.pdf"
    generate_pdf(out_file)
