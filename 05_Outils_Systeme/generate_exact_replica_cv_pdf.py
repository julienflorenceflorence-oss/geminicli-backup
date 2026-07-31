# -*- coding: utf-8 -*-
import os
import sys

# Ensure Python site-packages path is accessible
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
        self.rect(0, 0, 62, 297, 'F')
        
        # 3. Sidebar Divider Line (#D4AF37)
        self.set_draw_color(212, 175, 55)
        self.set_line_width(0.3)
        self.line(62, 0, 62, 297)

def clean_txt(text):
    for emoji in ["📞", "✉️", "📍", "🔗", "🏆", "📌", "😊", "🧐", "⚡", "🎯", "🤾", "✨", "📜", "📊", "💰", "💼", "🏢", "👤", "⚙️", "🎙️", "📩", "🤝", "🛏️", "🍽️", "🍸", "🚀", "🧠", "🏛️", "📐", "💬"]:
        text = text.replace(emoji, "")
    return text.replace("—", "-").replace("’", "'").replace("°", "o").replace("€", "EUR").replace("…", "...").replace("«", '"').replace("»", '"').replace("œ", "oe").replace("Œ", "OE")

def generate_pdf(out_path):
    pdf = ExactReplicaCVPDF()
    pdf.add_page()
    pdf.draw_layout()
    
    # ----------------------------------------------------
    # SIDEBAR CONTENT (Left Column, width 62mm)
    # ----------------------------------------------------
    
    # Profile Photo (Top Left)
    photo_path = "/Users/admin/.gemini/antigravity/brain/3b3f54ca-b09a-4ea4-9dc8-59a0af5a76aa/.user_uploaded/media__1785320733290.png"
    if os.path.exists(photo_path):
        pdf.image(photo_path, x=12, y=10, w=38, h=44)
        pdf.set_draw_color(212, 175, 55)
        pdf.set_line_width(0.5)
        pdf.rect(12, 10, 38, 44, 'D')
    
    # 4 Action Buttons
    buttons = [
        ("06 61 74 75 73", False, False),
        ("EMAIL", False, False),
        ("AGENDA", True, False),
        ("ACCES CV INTERACTIF", False, True)
    ]
    
    btn_y = 58
    for text, is_yellow, is_border_gold in buttons:
        if is_yellow:
            pdf.set_fill_color(234, 179, 8)
            pdf.set_draw_color(234, 179, 8)
            pdf.set_text_color(15, 17, 23)
        else:
            pdf.set_fill_color(20, 24, 34)
            pdf.set_draw_color(212, 175, 55) if is_border_gold else pdf.set_draw_color(60, 65, 80)
            pdf.set_text_color(248, 250, 252)
            
        pdf.set_font('Helvetica', 'B', 7)
        pdf.rect(8, btn_y, 46, 6.5, 'DF')
        pdf.set_xy(8, btn_y + 1.2)
        pdf.cell(46, 4, clean_txt(text), align='C')
        btn_y += 8.5
        
    # Sidebar Sections
    sidebar_sections = [
        ("EXPERTISES METIER", [
            "Management Hotelier & F&B",
            "Pilotage P&L (<60% Prime Cost)",
            "Revenue Mgt (Doyield)",
            "Virage MICE B2B Gare",
            "Management 30 ETP",
            "Smarketing & Bitrix24"
        ]),
        ("SOFT SKILLS", [
            "ENTJ-A | 94% Rationnel",
            "Sens de l'Organisation",
            "Leadership (Coach Handball)",
            "Sang-froid & Posture Girafe",
            "Culture Excellence & EX/UX"
        ]),
        ("LANGUES", [
            "Anglais : Courant (B2)",
            "Neerlandais : B2"
        ]),
        ("FORMATION", [
            "Bachelor Marketing (2025)",
            "HTML5 & CSS3 - Google"
        ])
    ]
    
    sec_y = 96
    for title, items in sidebar_sections:
        pdf.set_xy(8, sec_y)
        pdf.set_font('Times', 'B', 9)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(46, 4, clean_txt(title))
        
        pdf.set_draw_color(212, 175, 55)
        pdf.set_line_width(0.2)
        pdf.line(8, sec_y + 4.5, 54, sec_y + 4.5)
        
        sec_y += 6.5
        pdf.set_font('Helvetica', '', 6.8)
        pdf.set_text_color(203, 213, 225)
        
        for item in items:
            pdf.set_xy(8, sec_y)
            pdf.cell(3, 3.5, ">", align='L')
            pdf.set_xy(11, sec_y)
            pdf.multi_cell(43, 3.5, clean_txt(item))
            sec_y = pdf.get_y() + 0.5
            
        sec_y += 3
        
    # ----------------------------------------------------
    # MAIN CONTENT (Right Column, x=68mm to 200mm)
    # ----------------------------------------------------
    
    # Header Name
    pdf.set_xy(68, 12)
    pdf.set_font('Times', 'B', 22)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 8, clean_txt("JULIEN FLORENCE"))
    
    # Subtitle
    pdf.set_xy(68, 20)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(248, 250, 252)
    pdf.cell(132, 5, clean_txt("| MANAGER COMMERCIAL & OPERATIONNEL — JOST BORDEAUX"))
    
    # Profile Summary Paragraph
    pdf.set_xy(68, 27)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    summary = "Manager commercial et operationnel avec 15 ans d'experience dans l'animation d'equipes et la gestion de centres de profit (jusqu'a 2.6 M EUR). Alliant la rigueur operationnelle issue de l'hotellerie de luxe (Palaces 5* & Relais & Chateaux) a de solides competences en pilotage P&L, Revenue Management (Doyield) et developpement MICE B2B. Immediatement mobile et operationnel sur Bordeaux pour faire du site JOST Gare Saint-Jean le hub leader."
    pdf.multi_cell(132, 3.6, clean_txt(summary))
    
    # Section Title: EXPERIENCES PROFESSIONNELLES
    curr_y = pdf.get_y() + 4
    pdf.set_xy(68, curr_y)
    pdf.set_font('Times', 'B', 11)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(65, 5, clean_txt("EXPERIENCES PROFESSIONNELLES"))
    
    # Gold horizontal rule
    pdf.set_draw_color(212, 175, 55)
    pdf.set_line_width(0.3)
    pdf.line(133, curr_y + 3, 200, curr_y + 3)
    
    curr_y += 8
    
    # Experiences List
    jobs = [
        ("Directeur d'Hotel Hybride & F&B (Candidat)", "2026 - PRESENT", "JOST HOTEL BORDEAUX | MELT GROUP - GARE ST-JEAN", [
            "Conception d'un Plan d'Action Operationnel a 90 Jours ciblant le virage MICE B2B et Doyield.",
            "Commercialisation du Lieu Cheri et du Rooftop aupres des 50 grands comptes de la zone Gare.",
            "Operationalisation du Yield Management hybride (dortoirs vs chambres) et baisse des OTAs."
        ], ["MICE B2B", "Doyield", "P&L Management", "Rooftop & F&B"]),
        
        ("Responsable Developpement Commercial", "2025 - PRESENT", "HAPPY HOUSE | SOLUTIONS B2B & RENTABILITE", [
            "Management et coaching d'une equipe de 3 collaborateurs (animation, objectifs).",
            "Integration d'outils d'acquisition Tech, automatisation et suivi des KPIs de performance.",
            "Contribution directe aux projets transverses et a l'evolution des processus de vente."
        ], ["Management", "Processus", "KPIs"]),
        
        ("Gestionnaire de Centre de Profit & Manager", "2022 - 2024", "RAS INTERIM | LOGISTIQUE & SERVICES - CA 2.6 M EUR", [
            "Management quotidien de 20 ETP par semaine (formation, plannings, evaluations).",
            "Pilotage commercial : analyse des indicateurs cles et gestion de 25 comptes B2B.",
            "Garant du respect strict des meillerues procedures et de la conformite."
        ], ["Gestion d'equipe", "Indicateurs", "Procedures"]),
        
        ("Directeur de Restaurant & Centre de Profit", "2010 - 2015", "MA SALLE A MANGER | PARIS 1er - CA +140%", [
            "Animation quotidienne de l'espace de vente et management d'une equipe de 15 salaries.",
            "Pilotage de la rentabilite (comptes d'exploitation, P&L) : croissance de +140% du CA.",
            "Partenariats commerciaux B2B : galeries d'art, EVG/EVJF, mariages, Tour Operateurs."
        ], ["Gestion de stock", "P&L", "Animation"]),
        
        ("Management & Service d'Excellence", "2000 - 2009", "PALACES 5* & RESTAURANTS ETOILES | DUBLIN, ST-BARTH, ANGLETERRE", [
            "Management operationnel d'equipes de 7 a 20 collaborateurs (Guanahani Palace 5*).",
            "Fidelisation d'une clientele internationale selon les standards prestigieux LHW.",
            "Direction du service gastronomique Au Clos (Angleterre) et soirees oenologiques."
        ], ["Excellence", "Resolution de problemes", "Sommelier"])
    ]
    
    for role, dates, company, bullets, tags in jobs:
        # Job Role + Dates
        pdf.set_xy(68, curr_y)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(90, 4, clean_txt(role), align='L')
        
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(148, 163, 184)
        pdf.cell(42, 4, clean_txt(dates), align='R')
        
        # Company
        curr_y += 4.2
        pdf.set_xy(68, curr_y)
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(248, 250, 252)
        pdf.cell(132, 3.8, clean_txt(company))
        
        # Bullets
        curr_y += 4
        pdf.set_font('Helvetica', '', 7)
        pdf.set_text_color(203, 213, 225)
        for bullet in bullets:
            pdf.set_xy(68, curr_y)
            pdf.cell(3, 3.2, "-", align='L')
            pdf.set_xy(71, curr_y)
            pdf.multi_cell(129, 3.2, clean_txt(bullet))
            curr_y = pdf.get_y()
            
        # Tags (Pill Badges)
        curr_y += 1
        pdf.set_xy(68, curr_y)
        pdf.set_font('Helvetica', '', 6.2)
        pdf.set_text_color(212, 175, 55)
        pdf.set_draw_color(212, 175, 55)
        pdf.set_fill_color(20, 24, 34)
        
        tag_x = 68
        for tag in tags:
            tag_txt = clean_txt(f"({tag})")
            t_w = pdf.get_string_width(tag_txt) + 4
            if tag_x + t_w > 200:
                curr_y += 4.5
                tag_x = 68
            pdf.rect(tag_x, curr_y, t_w, 3.8, 'DF')
            pdf.set_xy(tag_x, curr_y + 0.4)
            pdf.cell(t_w, 3, tag_txt, align='C')
            tag_x += t_w + 2
            
        curr_y += 6

    pdf.output(out_path)
    print(f"✅ PDF Réplique Exacte généré : {out_path}")

if __name__ == "__main__":
    out_file = "Projets/prospection job/jost-hotel-bordeaux/04_Livrables/PDF/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.pdf"
    generate_pdf(out_file)
