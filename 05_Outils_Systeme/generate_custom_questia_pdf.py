#!/usr/bin/env python3
"""
Générateur dynamique et personnalisé des PDFs QuestIA LAB:
Intègre la charte graphique QuestIA LAB, le logo PNG officiel et les TEXTES PRÉ-ENREGISTRÉS des 4 types de PDF.
Permet d'injecter des données spécifiques (Nom Entreprise, Prospect, CA Export, Taux Fuite, Secteur, Remarque)
tout en conservant la structure intégrale du document choisi.
"""

import sys
import os
import argparse
import json
sys.path.insert(0, '/Users/admin/Library/Python/3.9/lib/python/site-packages')
from fpdf import FPDF

def clean_txt(text):
    if not text:
        return ""
    for emoji in ["📞", "✉️", "📍", "🔗", "🏆", "📌", "😊", "🧐", "⚡", "🎯", "🤾", "✨", "📜", "📊", "💰", "💼", "🏢", "👤", "⚙️", "🎙️", "📩", "🤝", "🚀", "🧠", "🏛️", "📐", "💬", "❌", "✅", "🎧", "🔬", "📌", "🟢", "🧪", "❓", "🌐", "📅", "📄", "▶"]:
        text = text.replace(emoji, "")
    return text.replace("—", "-").replace("’", "'").replace("°", "o").replace("€", "EUR").replace("…", "...").replace("«", '"').replace("»", '"').replace("œ", "oe").replace("Œ", "OE")

LOGO_PATH = '/Users/admin/Desktop/geminicli-backup/04_Livrables/Images/QuestIA_Lab_Logo.png'

SOURCES_LINKS = {
    "McKinsey & Co.": ("McKinsey & Co.", "Perte 3% a 5.4% marge nego B2B.", "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-pricing-revamp"),
    "Harvard Bus. Rev.": ("Harvard Bus. Rev.", "-30% impact persuasif langue 2.", "https://hbr.org/2012/04/the-foreign-language-effect"),
    "INSEAD Knowledge": ("INSEAD Knowledge", "Decodage psychologique DISC/PCM.", "https://www.insead.edu/executive-education/leadership/negotiation-dynamics"),
    "KPMG Global": ("KPMG Global", "72% blocages d'origine humaine.", "https://kpmg.com/xx/en/home/insights/2023/10/cross-border-ma.html"),
    "Business France": ("Business France", "68% concessions remises export.", "https://lelab.bpifrance.fr")
}

class QuestIALabCustomPDF(FPDF):
    def __init__(self, doc_type="DOCUMENT STRATEGIQUE", doc_title="QUESTIA LAB AUDIT", company_name="CLIENT"):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.doc_type = doc_type
        self.doc_title = doc_title
        self.company_name = company_name
        self.set_auto_page_break(auto=True, margin=12)

    def header(self):
        # Background page entière (QuestIA LAB Cyber Dark #05070D)
        self.set_fill_color(5, 7, 13)
        self.rect(0, 0, 210, 297, 'F')
        
        # Sidebar gauche (Gris Cyber #0B0F19, 55mm)
        self.set_fill_color(11, 15, 25)
        self.rect(0, 0, 55, 297, 'F')
        
        # Ligne verticale de séparation Cyan Néon #00E5FF
        self.set_draw_color(0, 229, 255)
        self.set_line_width(0.3)
        self.line(55, 0, 55, 297)

        # Insertion du Logo QuestIA LAB dans la Sidebar
        if os.path.exists(LOGO_PATH):
            self.image(LOGO_PATH, x=8.5, y=5, w=38)
            y_sidebar_start = 32
        else:
            self.set_xy(5, 8)
            self.set_font('Times', 'B', 14)
            self.set_text_color(0, 229, 255)
            self.cell(45, 6, "QUESTIA LAB", align='C')
            y_sidebar_start = 16

        self.set_xy(5, y_sidebar_start)
        self.set_font('Helvetica', 'B', 5.8)
        self.set_text_color(123, 92, 255) # Violet #7B5CFF
        self.cell(45, 3.5, "DECISION & BEHAVIOR ACCELERATOR", align='C')
        
        self.set_draw_color(0, 229, 255)
        self.set_line_width(0.2)
        self.line(10, y_sidebar_start + 4.5, 45, y_sidebar_start + 4.5)

        # Contact info sidebar
        y_c = y_sidebar_start + 7
        self.set_xy(5, y_c)
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(0, 229, 255)
        self.cell(45, 3.5, "AUDITEUR EXECUTIF", align='L')
        
        self.set_font('Helvetica', '', 6.2)
        self.set_text_color(226, 232, 240)
        contacts = [
            "Julien FLORENCE",
            "Dir. Strategie & Growth",
            "Tel : 06 61 74 75 73",
            "julien.florence@email.com",
            "Toulouse | France"
        ]
        y_c += 4.0
        for c in contacts:
            self.set_xy(5, y_c)
            self.cell(45, 3.2, clean_txt(c), align='L')
            y_c += 3.5

        self.set_draw_color(0, 229, 255)
        self.set_line_width(0.2)
        self.line(5, y_c + 2, 50, y_c + 2)

        # En-tête Main Content (x=62mm)
        self.set_xy(62, 5)
        self.set_font('Helvetica', 'B', 7.0)
        self.set_text_color(0, 229, 255) # Cyan Néon
        self.cell(138, 3.5, clean_txt(f"{self.doc_type.upper()} | {self.company_name.upper()}"), align='L')
        
        self.set_xy(62, 8.5)
        self.set_font('Times', 'B', 9.5)
        self.set_text_color(248, 250, 252) # Blanc
        self.multi_cell(138, 4.0, clean_txt(self.doc_title), align='L')
        
        y_line = max(19, self.get_y() + 1.5)
        self.set_draw_color(0, 229, 255)
        self.set_line_width(0.4)
        self.line(62, y_line, 200, y_line)

    def footer(self):
        self.set_y(-10)
        self.set_font('Helvetica', '', 6.8)
        self.set_text_color(148, 163, 184)
        self.set_x(62)
        self.cell(138, 5, clean_txt(f"QuestIA LAB - Audit Personnalise pour {self.company_name} | Page {self.page_no()}"), align='R')

def draw_sidebar_sources(pdf, y_start):
    pdf.set_xy(5, y_start)
    pdf.set_font('Times', 'B', 7.5)
    pdf.set_text_color(0, 229, 255)
    pdf.cell(45, 4, "SOURCES ET PREUVES (CLIQUABLES)", align='L')
    
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(5, y_start + 4.5, 50, y_start + 4.5)
    
    y = y_start + 6
    for key, (title, desc, url) in SOURCES_LINKS.items():
        pdf.set_xy(5, y)
        pdf.set_font('Helvetica', 'B', 6.5)
        pdf.set_text_color(0, 229, 255)
        pdf.cell(45, 3.2, clean_txt(f"> {title}"), align='L', link=url)
        y += 3.2
        pdf.set_xy(5, y)
        pdf.set_font('Helvetica', '', 5.8)
        pdf.set_text_color(226, 232, 240)
        pdf.multi_cell(45, 2.7, clean_txt(desc), align='L')
        y += 6.2

def generate_custom_pdf(data, out_path):
    company = data.get("company", "ENTREPRISE CIBLE")
    prospect = data.get("prospect", "Monsieur / Madame le Directeur")
    title_prospect = data.get("title_prospect", "Directeur Général / VP Sales")
    sector = data.get("sector", "Aéronautique & Export")
    revenue = data.get("revenue", "10 000 000 EUR")
    leak_rate = float(data.get("leak_rate", 4.2))
    pdf_type = data.get("pdf_type", "choc_refus")
    custom_note = data.get("custom_note", "")

    rev_val = float(revenue.replace(" ", "").replace("EUR", "").replace("€", "") or 10000000)
    est_loss = int(rev_val * (leak_rate / 100.0))

    if pdf_type == "confirmatif":
        doc_type = "CONFIRMATION & PREPARATION AUDIT"
        doc_title = f"AUDIT DE PERFORMANCE COMMERCIALE - {company.upper()}"
        pdf = QuestIALabCustomPDF(doc_type, doc_title, company)
        pdf.add_page()
        draw_sidebar_sources(pdf, 65)

        pdf.set_xy(62, 23)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt(f"DOCUMENT A L'ATTENTION DE : {prospect.upper()} ({title_prospect.upper()})"))

        pdf.set_xy(62, 29)
        pdf.set_font('Helvetica', '', 7.5)
        pdf.set_text_color(226, 232, 240)
        p_intro = f"Nous vous confirmons la tenue de votre session d'Audit de Performance Commerciale & Decodage Comportemental en Visio (30 min) pour {company}. Cet entretien permettra d'evaluer la fermete tactique de vos forces de vente sur votre secteur ({sector}) et sur votre volume export (estime a {revenue})."
        pdf.multi_cell(138, 3.5, clean_txt(p_intro), align='J')

        # Agenda 30 min
        pdf.set_xy(62, 45)
        pdf.set_font('Times', 'B', 10)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt("1. DEROULE ET ORDRE DU JOUR DE L'AUDIT (30 MIN VISIO)"))
        pdf.set_draw_color(0, 229, 255)
        pdf.set_line_width(0.2)
        pdf.line(62, 50, 200, 50)

        steps = [
            ("Etape 1 (10 min) - Evaluation des 5 Frictions d'Impact", f"Analyse factuelle des negociations internationales recentes de {company} et chiffrage du taux de fuite de marge ({leak_rate}% est.)."),
            ("Etape 2 (10 min) - Passation du Diagnostic Psychometrique (PCM/DISC)", "Evaluation orale de la grille de lecture comportementale des commerciaux sous la pression d'interlocuteurs internationaux."),
            ("Etape 3 (10 min) - Restitution & Demonstration du Simulateur IA", "Restitution de l'audit et demonstration de la boucle d'immersion tactique QuestIA LAB (Offre High-Ticket 2 000 EUR HT).")
        ]

        cur_y = 52
        for st_title, st_desc in steps:
            pdf.set_xy(62, cur_y)
            pdf.set_font('Helvetica', 'B', 7.5)
            pdf.set_text_color(0, 229, 255)
            pdf.multi_cell(138, 3.5, clean_txt(st_title), align='L')
            cur_y += 4.0
            pdf.set_xy(62, cur_y)
            pdf.set_font('Helvetica', '', 6.8)
            pdf.set_text_color(200, 205, 215)
            pdf.multi_cell(138, 3.1, clean_txt(st_desc), align='L')
            cur_y += 7.0

        if custom_note:
            pdf.set_xy(62, cur_y + 2)
            pdf.set_font('Helvetica', 'I', 7.0)
            pdf.set_text_color(248, 250, 252)
            pdf.multi_cell(138, 3.0, clean_txt(f"Note de l'Auditeur : {custom_note}"), align='L')

    elif pdf_type == "choc_refus":
        doc_type = "NOTE D'IMPACT STRATEGIQUE FINANCIER"
        doc_title = f"CHOC FINANCIER : LE COUT DE L'INACTION POUR {company.upper()}"
        pdf = QuestIALabCustomPDF(doc_type, doc_title, company)
        pdf.add_page()
        draw_sidebar_sources(pdf, 65)

        pdf.set_xy(62, 23)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt(f"A L'ATTENTION DE : {prospect.upper()} ({title_prospect.upper()})"))

        pdf.set_xy(62, 29)
        pdf.set_font('Helvetica', '', 7.5)
        pdf.set_text_color(226, 232, 240)
        p_choc = f"Chaque negociation internationale menee par {company} sans decodage psychologique de l'acheteur etranger est une fuite directe de profit net. Penser que vos commerciaux 'maitrisent l'anglais' masque une realite financiere critique : la perte d'impact et de fermete sous pression."
        pdf.multi_cell(138, 3.5, clean_txt(p_choc), align='J')

        # Simulation Financière Personnalisée
        pdf.set_xy(62, 43)
        pdf.set_font('Times', 'B', 10)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt(f"1. CHIFFRAGE DU MANQUE A GAGNER POUR {company.upper()}"))
        pdf.set_draw_color(0, 229, 255)
        pdf.set_line_width(0.2)
        pdf.line(62, 48, 200, 48)

        pdf.set_xy(62, 51)
        pdf.set_fill_color(20, 24, 34)
        pdf.set_draw_color(0, 229, 255)
        pdf.rect(62, 51, 138, 18, 'DF')

        pdf.set_xy(64, 53)
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(248, 250, 252)
        pdf.multi_cell(134, 3.2, clean_txt(f"Chiffre d'Affaires Export Estime ({sector}) : {revenue}"), align='L')

        pdf.set_xy(64, 57)
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(134, 3.2, clean_txt(f"Taux de Fuite de Marge Sous Pression : {leak_rate} %"), align='L')

        pdf.set_xy(64, 61)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(123, 92, 255)
        pdf.multi_cell(134, 3.8, clean_txt(f"Perte de Profits Nets Estimee : {est_loss:,} EUR / an"), align='L')

        # Les 3 Illusions
        pdf.set_xy(62, 73)
        pdf.set_font('Times', 'B', 10)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt("2. LES 3 ILLUSIONS DANGEREUSES QUI COUTENT DE LA MARGE"))
        pdf.set_draw_color(0, 229, 255)
        pdf.set_line_width(0.2)
        pdf.line(62, 78, 200, 78)

        illusions = [
            ("Illusion #1 : 'Nos commerciaux parlent couramment anglais'", "Parler anglais n'a aucun rapport avec la maitrise de la posture de pouvoir sous pression. L'INSEAD prouve qu'un cadre perd 30% d'impact persuasif en langue seconde face a un acheteur agressif."),
            ("Illusion #2 : 'Les cours de langues ou le CPF suffisent'", "Les cours traditionnels apprennent le vocabulaire, pas le decodage psychologique (PCM/DISC). QuestIA LAB est un simulateur tactique d'immersion haute-performance (2 000 EUR HT)."),
            ("Illusion #3 : 'Le probleme vient du prix ou de la concurrence'", "Faux. KPMG démontre que dans 72% des cas, les blocages sont dus a une mauvaise lecture du profil du decisionnaire.")
        ]

        cur_y = 80
        for ill_title, ill_desc in illusions:
            pdf.set_xy(62, cur_y)
            pdf.set_font('Helvetica', 'B', 7.2)
            pdf.set_text_color(248, 250, 252)
            pdf.multi_cell(138, 3.5, clean_txt(ill_title), align='L')
            cur_y += 3.6
            pdf.set_xy(65, cur_y)
            pdf.set_font('Helvetica', '', 6.6)
            pdf.set_text_color(160, 164, 176)
            pdf.multi_cell(135, 2.9, clean_txt(ill_desc), align='L')
            cur_y += 6.5

    elif pdf_type == "passe_barrage":
        doc_type = "NOTE D'INFORMATION EXECUTIVE"
        doc_title = f"AUDIT EXECUTIVE MARGES EXPORT - A L'ATTENTION DE {company.upper()}"
        pdf = QuestIALabCustomPDF(doc_type, doc_title, company)
        pdf.add_page()
        draw_sidebar_sources(pdf, 65)

        pdf.set_xy(62, 23)
        pdf.set_fill_color(20, 24, 34)
        pdf.set_draw_color(0, 229, 255)
        pdf.set_line_width(0.3)
        pdf.rect(62, 23, 138, 12, 'DF')

        pdf.set_xy(64, 24.5)
        pdf.set_font('Helvetica', 'B', 7.0)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(134, 3.2, clean_txt(f"A L'ATTENTION DU SECRETARIAT DE DIRECTION DE {company.upper()} :"), align='L')

        pdf.set_xy(64, 28.0)
        pdf.set_font('Helvetica', 'I', 6.5)
        pdf.set_text_color(248, 250, 252)
        pdf.multi_cell(134, 2.9, clean_txt(f"Ce document de synthese contient les donnees d'audit de marge pour {prospect} ({title_prospect}). Merci de le lui remettre en main propre."), align='L')

        pdf.set_xy(62, 38)
        pdf.set_font('Times', 'B', 10)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt("1. RESUME EXECUTIF DE LA MISSION D'AUDIT"))
        pdf.set_draw_color(0, 229, 255)
        pdf.set_line_width(0.2)
        pdf.line(62, 43, 200, 43)

        pdf.set_xy(62, 45)
        pdf.set_font('Helvetica', '', 7.0)
        pdf.set_text_color(226, 232, 240)
        p_pass = f"QuestIA LAB conduit actuellement un audit national sur le secteur {sector}. Pour {company} (CA export {revenue}), les pertes de marge sous pression representent un enjeu direct de {est_loss:,} EUR par an."
        pdf.multi_cell(138, 3.2, clean_txt(p_pass), align='J')

    else:
        doc_type = "GUIDE SECTORIEL & DIAGNOSTIC"
        doc_title = f"DIAGNOSTIC SUR-MESURE SECTEUR {sector.upper()}"
        pdf = QuestIALabCustomPDF(doc_type, doc_title, company)
        pdf.add_page()
        draw_sidebar_sources(pdf, 65)

        pdf.set_xy(62, 23)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt(f"SCRIPT & DIAGNOSTIC SECTORIEL : {sector.upper()}"))

        pdf.set_xy(62, 30)
        pdf.set_font('Helvetica', '', 7.5)
        pdf.set_text_color(226, 232, 240)
        pdf.multi_cell(138, 3.5, clean_txt(f"Diagnostic prepare sur-mesure pour {prospect} ({title_prospect}) chez {company}. Taux de concession cible : {leak_rate}% sur {revenue} de CA Export."), align='J')

    # Action call box (always present)
    pdf.set_xy(62, 115)
    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.4)
    pdf.rect(62, 115, 138, 14, 'DF')

    pdf.set_xy(64, 116.5)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(134, 3.5, clean_txt(f"PLANIFIER L'AUDIT STRATEGIQUE DE 30 MIN POUR {company.upper()}"), align='C')

    pdf.set_xy(64, 120.5)
    pdf.set_font('Helvetica', '', 6.6)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 3.0, clean_txt("Session individuelle reservee a la Direction Commerciale & Export."), align='C')

    pdf.set_xy(64, 124.0)
    pdf.set_font('Helvetica', 'U', 6.5)
    pdf.set_text_color(0, 229, 255)
    url_choc = "https://julienflorenceflorence-oss.github.io/cv-prestige/"
    pdf.cell(134, 3.0, clean_txt("Prendre rendez-vous avec Julien FLORENCE (06 61 74 75 73) >"), align='C', link=url_choc)

    pdf.output(out_path)
    print(f"✅ PDF Personnalisé avec texte intégral généré : {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur de PDF QuestIA LAB Personnalisé")
    parser.add_argument("--json", type=str, help="Fichier JSON de configuration")
    parser.add_argument("--company", type=str, default="Airbus Subcontractor")
    parser.add_argument("--prospect", type=str, default="Jean DUPONT")
    parser.add_argument("--title", type=str, default="VP Sales Export")
    parser.add_argument("--sector", type=str, default="Aéronautique")
    parser.add_argument("--revenue", type=str, default="15 000 000 EUR")
    parser.add_argument("--leak", type=float, default=4.2)
    parser.add_argument("--type", type=str, default="choc_refus")
    parser.add_argument("--out", type=str, default="04_Livrables/PDF/05_QUESTIA LAB_Audit_Personnalise.pdf")

    args = parser.parse_args()

    data = {
        "company": args.company,
        "prospect": args.prospect,
        "title_prospect": args.title,
        "sector": args.sector,
        "revenue": args.revenue,
        "leak_rate": args.leak,
        "pdf_type": args.type
    }

    if args.json:
        if os.path.exists(args.json):
            with open(args.json, 'r') as f:
                data = json.load(f)
        else:
            data = json.loads(args.json)

    out_path = args.out
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    generate_custom_pdf(data, out_path)
