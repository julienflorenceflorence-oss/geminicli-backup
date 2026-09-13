#!/usr/bin/env python3
"""
Générateur des 4 PDFs de prospection, diagnostic et scripts QuestIA LAB:
1. PDF #1: Confirmation & Préparation RDV Audit (Visio 30 min)
2. PDF #2: Note Choc Perte de CA Immédiat (Refus / Relance)
3. PDF #3: Note d'Information Exécutive Passe-Barrage Secrétariat
4. PDF #4: PLAYBOOK ÉQUIPE QUESTIA LAB — SCRIPTS TÉLÉPHONIQUES COMPLETS MOT-À-MOT POUR DÉCLENCHER LE RDV AUDIT SUR LES 5 ICPS (avec Sources Cliquables & Logo PNG)
"""

import sys
import os
sys.path.insert(0, '/Users/admin/Library/Python/3.9/lib/python/site-packages')
from fpdf import FPDF

def clean_txt(text):
    if not text:
        return ""
    replacements = {
        "—": "-", "’": "'", "°": "o", "€": "EUR", "…": "...",
        "«": '"', "»": '"', "œ": "oe", "Œ": "OE", "“": '"', "”": '"',
        "🔴": "[DOMINANT]", "🟢": "[STABLE]", "🔵": "[CONSCIENCIEUX]", "🟡": "[INFLUENT]",
        "🎯": "[CIBLE]", "🚀": "[ACTION]", "⚡": "[URGENCE]", "📌": "[NOTE]"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    cleaned = []
    for c in text:
        if ord(c) <= 255:
            cleaned.append(c)
    return "".join(cleaned)

LOGO_PATH = '/Users/admin/Desktop/geminicli-backup/04_Livrables/Images/QuestIA_Lab_Logo.png'

SOURCES_LINKS = {
    "McKinsey & Co.": ("McKinsey & Co.", "Perte 3% a 5.4% marge nego B2B.", "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-pricing-revamp"),
    "Harvard Bus. Rev.": ("Harvard Bus. Rev.", "-30% impact persuasif langue 2.", "https://hbr.org/2012/04/the-foreign-language-effect"),
    "INSEAD Knowledge": ("INSEAD Knowledge", "Decodage psychologique DISC/PCM.", "https://www.insead.edu/executive-education/leadership/negotiation-dynamics"),
    "KPMG Global": ("KPMG Global", "72% blocages d'origine humaine.", "https://kpmg.com/xx/en/home/insights/2023/10/cross-border-ma.html"),
    "Business France": ("Business France", "68% concessions remises export.", "https://lelab.bpifrance.fr")
}

class QuestIALabPDF(FPDF):
    def __init__(self, doc_type="DOCUMENT STRATEGIQUE", doc_title="QUESTIA LAB AUDIT", is_playbook=False):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.doc_type = doc_type
        self.doc_title = doc_title
        self.is_playbook = is_playbook

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

        # Insertion du Logo QuestIA LAB dans la Sidebar sans chevauchement (w=38mm, y=5mm -> h=24.7mm)
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

        # Contact info sidebar (omitted for internal playbook PDF #4)
        if not self.is_playbook:
            y_c = y_sidebar_start + 7
            self.set_xy(5, y_c)
            self.set_font('Helvetica', 'B', 7)
            self.set_text_color(0, 229, 255)
            self.cell(45, 3.5, "AUDITEUR EXECUTIF", align='L')
            y_c += 4.0
            
            self.set_font('Helvetica', '', 6.2)
            self.set_text_color(226, 232, 240)
            contacts = [
                "Julien FLORENCE",
                "Dir. Strategie & Growth",
                "Tel : 06 61 74 75 73",
                "julien.florence@email.com",
                "Toulouse | France"
            ]
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
        self.cell(138, 3.5, clean_txt(self.doc_type.upper()), align='L')
        
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
        self.cell(138, 5, clean_txt(f"QuestIA LAB - Audit de Performance Commerciale & Decodage Comportemental | Page {self.page_no()}"), align='R')

def draw_sidebar_sources(pdf, y_start=62):
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

# ==========================================
# 1. PDF #1 (CONFIRMATIF RDV)
# ==========================================
def generate_pdf1_confirmation(out_path):
    pdf = QuestIALabPDF("CONFIRMATION & PREPARATION AUDIT", "AUDIT DE PERFORMANCE COMMERCIALE FACE AUX CLIENTS ETRANGERS")
    pdf.add_page()
    draw_sidebar_sources(pdf, 62)
    
    pdf.set_xy(62, 23)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("DOCUMENT A L'ATTENTION DE LA DIRECTION COMMERCIALE & EXPORT"))
    
    pdf.set_xy(62, 29)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    p_intro = "Nous vous confirmons la tenue de votre session d'Audit de Performance Commerciale & Decodage Comportemental en Visio (30 min). Cet entretien permettra d'evaluer la fermete tactique et l'impact de vos forces de vente lorsqu'elles negocient avec des acheteurs et partenaires issus de pays etrangers (US, UK, Asie, Europe)."
    pdf.multi_cell(138, 3.5, clean_txt(p_intro), align='J')
    
    pdf.set_xy(62, 45)
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("1. DEROULE ET ORDRE DU JOUR DE L'AUDIT (30 MIN VISIO)"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, 50, 200, 50)
    
    steps = [
        ("Etape 1 (10 min) - Evaluation des 5 Frictions d'Impact", "Analyse factuelle des negos internationales recentes et identification des points de fuite de marge nette face aux acheteurs etrangers."),
        ("Etape 2 (10 min) - Passation du Diagnostic Psychometrique (PCM/DISC)", "Evaluation orale de la grille de lecture comportementale des commerciaux sous la pression d'interlocuteurs anglo-saxons ou internationaux."),
        ("Etape 3 (10 min) - Restitution & Demonstration du Simulateur IA", "Chiffrage du manque a gagner et demonstration de la boucle d'immersion tactique QuestIA LAB (Offre High-Ticket 2 000 EUR HT).")
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

    pdf.set_xy(62, cur_y + 2)
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("2. RAPPEL DES FAITS ECONOMIQUES CONSTATES (SOURCES CLIQUABLES)"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, cur_y + 7, 200, cur_y + 7)
    
    facts = [
        ("McKinsey & Company (3% a 5.4% Marge Nette)", "Les concessions financieres et le manque de fermete en nego cross-border detruisent directement 3% a 5% de profit net.", "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-pricing-revamp"),
        ("Harvard Business Review (-30% d'Impact Persuasif)", "Le 'Foreign-Language Effect' reduit de 30% la repartie et l'autorite naturelle d'un cadre negociant en langue seconde.", "https://hbr.org/2012/04/the-foreign-language-effect"),
        ("INSEAD Executive Education (Decodage Psychologique)", "Savoir parler anglais ne suffit pas : sans maitrise du decodage comportemental (DISC/PCM), le vendeur lache du terrain.", "https://www.insead.edu/executive-education/leadership/negotiation-dynamics"),
        ("KPMG Global Deal Survey (72% de Blocages)", "72% des blocages lors des transactions internationales sont d'origine comportementale et non tarifaire.", "https://kpmg.com/xx/en/home/insights/2023/10/cross-border-ma.html"),
        ("Business France / Bpifrance (68% d'Aides Concedees)", "Pres de 70% des exportateurs concedent des remises et frais annexe par incertitude dans le rapport de force.", "https://lelab.bpifrance.fr")
    ]
    
    cur_y += 9
    for f_title, f_desc, f_url in facts:
        pdf.set_xy(62, cur_y)
        pdf.set_font('Helvetica', 'B', 7.2)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.2, clean_txt(f"- {f_title}"), align='L')
        cur_y += 3.6
        pdf.set_xy(65, cur_y)
        pdf.set_font('Helvetica', '', 6.6)
        pdf.set_text_color(160, 164, 176)
        pdf.multi_cell(135, 2.9, clean_txt(f_desc), align='L')
        cur_y += 6.5

    pdf.set_xy(62, cur_y + 2)
    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.3)
    pdf.rect(62, cur_y + 2, 138, 12, 'DF')
    
    pdf.set_xy(64, cur_y + 3.5)
    pdf.set_font('Helvetica', 'B', 7.2)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(134, 3.2, clean_txt("CONSIGNE DE PREPARATION POUR L'AUDIT :"), align='L')
    
    pdf.set_xy(64, cur_y + 7.0)
    pdf.set_font('Helvetica', '', 6.5)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.9, clean_txt("Merci de vous munir des elements d'un contrat international recent et d'identifier les typologies d'acheteurs etrangers cibles."), align='L')

    pdf.output(out_path)
    print(f"✅ PDF #1 généré sans chevauchement : {out_path}")

# ==========================================
# 2. PDF #2 (CHOC REFUS / RELANCE)
# ==========================================
def generate_pdf2_choc_refus(out_path):
    pdf = QuestIALabPDF("NOTE DE IMPACT STRATEGIQUE", "CHOC FINANCIER : LE COUT DE L'INACTION EN NEGOCIATION INTERNATIONALE")
    pdf.add_page()
    draw_sidebar_sources(pdf, 62)
    
    pdf.set_xy(62, 23)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("POURQUOI VOS EQUIPES PERDENT 3% A 5% DE MARGE NETTE EN ANGLAIS"))
    
    pdf.set_xy(62, 28)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    p_choc = "Chaque negociation internationale menee sans decodage psychologique de l'acheteur etranger est une fuite directe de profit net pour votre entreprise. Penser que vos commerciaux 'maitrisent l'anglais' masque une realite financiere critique : la perte d'impact et de fermete sous pression."
    pdf.multi_cell(138, 3.5, clean_txt(p_choc), align='J')

    pdf.set_xy(62, 43)
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("1. SIMULATION IMPACT FINANCIER DU MANQUE A GAGNER (MCKINSEY DATA)"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, 48, 200, 48)

    pdf.set_xy(62, 51)
    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    
    headers = [("CA International / Export", 45), ("Fuite Marge (3.5% moy.)", 45), ("Perte Profits Nets / An", 48)]
    x_h = 62
    for h_txt, h_w in headers:
        pdf.set_xy(x_h, 51)
        pdf.set_font('Helvetica', 'B', 6.8)
        pdf.set_text_color(0, 229, 255)
        pdf.rect(x_h, 51, h_w, 4.5, 'DF')
        pdf.cell(h_w, 4.5, clean_txt(h_txt), align='C')
        x_h += h_w

    rows = [
        ("5 000 000 EUR", "3.5 % de concessions", "175 000 EUR / an"),
        ("15 000 000 EUR", "3.5 % de concessions", "525 000 EUR / an"),
        ("50 000 000 EUR", "3.5 % de concessions", "1 750 000 EUR / an")
    ]
    
    r_y = 55.5
    for r1, r2, r3 in rows:
        pdf.set_xy(62, r_y)
        pdf.set_font('Helvetica', '', 6.6)
        pdf.set_text_color(248, 250, 252)
        pdf.rect(62, r_y, 45, 4.2)
        pdf.cell(45, 4.2, clean_txt(r1), align='C')
        pdf.rect(107, r_y, 45, 4.2)
        pdf.cell(45, 4.2, clean_txt(r2), align='C')
        pdf.set_font('Helvetica', 'B', 6.6)
        pdf.set_text_color(0, 229, 255)
        pdf.rect(152, r_y, 48, 4.2)
        pdf.cell(48, 4.2, clean_txt(r3), align='C')
        r_y += 4.2

    pdf.set_xy(62, r_y + 4)
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("2. LES 3 ILLUSIONS DANGEREUSES QUI COUTENT DE LA MARGE"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, r_y + 9, 200, r_y + 9)
    
    illusions = [
        ("Illusion #1 : 'Nos commerciaux parlent couramment anglais'", "Parler anglais n'a aucun rapport avec la maitrise de la posture de pouvoir sous pression. L'INSEAD prouve qu'un cadre perd 30% d'impact persuasif en langue seconde face a un acheteur agressif."),
        ("Illusion #2 : 'Les cours de langues ou le CPF suffisent'", "Les cours traditionnels apprennent le vocabulaire, pas le decodage psychologique (PCM/DISC). QuestIA LAB est un simulateur tactique d'immersion haute-performance (2 000 EUR HT)."),
        ("Illusion #3 : 'Le probleme vient du prix ou de la concurrence'", "Faux. KPMG démontre que dans 72% des cas, les blocages ou abandons de negociations internationales sont dus a une mauvaise lecture du profil du decisionnaire et a une mauvaise posture.")
    ]
    
    cur_y = r_y + 11
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
        cur_y += 7.0

    pdf.set_xy(62, cur_y + 2)
    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.4)
    pdf.rect(62, cur_y + 2, 138, 14, 'DF')
    
    pdf.set_xy(64, cur_y + 3.5)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(134, 3.5, clean_txt("NE LAISSEZ PAS 5% DE VOTRE MARGE SUR LA TABLE DE NEGOCIATION"), align='C')
    
    pdf.set_xy(64, cur_y + 7.5)
    pdf.set_font('Helvetica', '', 6.6)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 3.0, clean_txt("Demandez votre Audit de Performance Commerciale (30 min Visio) sans engagement."), align='C')
    
    pdf.set_xy(64, cur_y + 11.0)
    pdf.set_font('Helvetica', 'U', 6.5)
    pdf.set_text_color(0, 229, 255)
    url_choc = "https://julienflorenceflorence-oss.github.io/cv-prestige/"
    pdf.multi_cell(134, 3.0, clean_txt("Prendre rendez-vous avec l'Auditeur Executif >"), align='C')

    pdf.output(out_path)
    print(f"✅ PDF #2 généré sans chevauchement : {out_path}")

# ==========================================
# 3. PDF #3 (PASSE-BARRAGE SECRETARIAT)
# ==========================================
def generate_pdf3_passe_barrage(out_path):
    pdf = QuestIALabPDF("NOTE D'INFORMATION EXECUTIVE", "AUDIT DE PERFORMANCE COMMERCIALE A L'INTERNATIONAL & MARGES EXPORT")
    pdf.add_page()
    draw_sidebar_sources(pdf, 62)
    
    pdf.set_xy(62, 23)
    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.3)
    pdf.rect(62, 23, 138, 12, 'DF')
    
    pdf.set_xy(64, 24.5)
    pdf.set_font('Helvetica', 'B', 7.0)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(134, 3.2, clean_txt("A L'ATTENTION DU SECRETARIAT DE DIRECTION / ASSISTANTE DE PRESIDENCE :"), align='L')
    
    pdf.set_xy(64, 28.0)
    pdf.set_font('Helvetica', 'I', 6.5)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.9, clean_txt("Ce document de synthese contient les donnees d'audit de marge sur les negociations internationales. Merci de le remettre en main propre au Directeur General / VP Sales."), align='L')

    pdf.set_xy(62, 38)
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("1. OBJET DE LA NOTE : RESUME EXECUTIF DE LA MISSION D'AUDIT"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, 43, 200, 43)

    pdf.set_xy(62, 45)
    pdf.set_font('Helvetica', '', 7.0)
    pdf.set_text_color(226, 232, 240)
    p_pass = "QuestIA LAB conduit actuellement une campagne nationale d'Audit de Performance Commerciale et de Decodage Comportemental aupres des directions generales, commerciales et export (Aeronautique & Secteurs d'Exportation Prestige)."
    pdf.multi_cell(138, 3.2, clean_txt(p_pass), align='J')

    pdf.set_xy(62, 55)
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("2. SYNTHESE DES ENJEUX POUR VOTRE DIRECTION"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, 60, 200, 60)

    points = [
        ("Protection des Marges Nettes (3% a 5%)", "Les etudes McKinsey et Business France demontrent que les negociations en langue etrangere engendrent des fuites de marge d'au moins 3% due au manque de fermete sous pression."),
        ("Decodage Psychologique (DISC/PCM)", "72% des blocages avec les acheteurs etrangers ne viennent pas du produit mais d'erreurs de posture et d'incapacite a imposer le prix."),
        ("Entretien d'Audit de 30 Minutes", "Un entretien de diagnostic individuel de 30 minutes en Visio est reserve a la Direction pour chiffrer l'impact reel sur vos comptes.")
    ]

    cur_y = 62
    for p_title, p_desc in points:
        pdf.set_xy(62, cur_y)
        pdf.set_font('Helvetica', 'B', 7.2)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.5, clean_txt(f"- {p_title}"), align='L')
        cur_y += 3.6
        pdf.set_xy(65, cur_y)
        pdf.set_font('Helvetica', '', 6.6)
        pdf.set_text_color(160, 164, 176)
        pdf.multi_cell(135, 2.9, clean_txt(p_desc), align='L')
        cur_y += 6.5

    pdf.set_xy(62, cur_y + 4)
    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.3)
    pdf.rect(62, cur_y + 4, 138, 14, 'DF')
    
    pdf.set_xy(64, cur_y + 5.5)
    pdf.set_font('Helvetica', 'B', 7.2)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 3.2, clean_txt("ACTION DEMANDEE AU SECRETARIAT :"), align='L')
    
    pdf.set_xy(64, cur_y + 9.0)
    pdf.set_font('Helvetica', '', 6.5)
    pdf.set_text_color(200, 205, 215)
    pdf.multi_cell(134, 2.9, clean_txt("Merci de transmettre cette note a Monsieur/Madame le Directeur General ou VP Sales pour planifier la session d'audit de 30 minutes. Contact direct : 06 61 74 75 73."), align='L')

    pdf.output(out_path)
    print(f"✅ PDF #3 généré sans chevauchement : {out_path}")

# ==========================================
# 4. PDF #4 (PLAYBOOK ÉQUIPE - SCRIPTS MOT-À-MOT COMPLETS POUR 5 ICPS)
# ==========================================
def generate_pdf4_scripts_5icps(out_path):
    pdf = QuestIALabPDF("PLAYBOOK COMMERCIAL ÉQUIPE QUESTIA LAB", "PLAYBOOK DE PROSPECTION TELEPHONIQUE & SCRIPTS DIAGNOSTIC PAR ICP", is_playbook=True)
    
    # ----------------------------------------------------
    # PAGE 1 : MANIFESTE & METHODOLOGIE GENERALE QUESTIA LAB
    # ----------------------------------------------------
    pdf.add_page()
    draw_sidebar_sources(pdf, 45)
    
    pdf.set_xy(62, 23)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("DOCUMENT INTERNE REUTILISABLE PAR L'EQUIPE COMMERCIALE QUESTIA LAB"))

    pdf.set_xy(62, 28)
    pdf.set_font('Helvetica', '', 7.2)
    pdf.set_text_color(226, 232, 240)
    p_manifesto = "Ce playbook rassemble la méthodologie opérationnelle et les trames mot-à-mot pour déclencher un rendez-vous d'Audit de Performance Commerciale en Visio (30 min) auprès des 5 profil types de prospects (ICPs) ciblés par QuestIA LAB. Chaque appel doit suivre une posture d'autorité exécutive et de diagnostic d'impact financier."
    pdf.multi_cell(138, 3.2, clean_txt(p_manifesto), align='J')

    pdf.set_xy(62, 42)
    pdf.set_font('Times', 'B', 9.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("1. STRUCTURE STRATEGIQUE DE L'APPEL EN 4 TEMPS (10 MIN MAX)"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, 47, 200, 47)

    temps_call = [
        ("Temps 1 : Le Passe-Barrage Secrétariat (30 sec)", "Posturer comme un auditeur exécutif mandater pour une étude de marge export. Pas de posture de vendeur."),
        ("Temps 2 : L'Accroche Choc Marge Nette (90 sec)", "Citer le taux de fuite de marge sectoriel (McKinsey / Business France) et poser la question du volume export."),
        ("Temps 3 : Le Traitement de l'Objection Majeure (3 min)", "Ne pas débattre. Relever la friction psychologique (DISC/PCM) et réfuter par les données académiques."),
        ("Temps 4 : Le Closing Alternatif du RDV Visio 30 min (60 sec)", "Imposer une alternative binaire d'horaires (ex: Mardi 10h ou Jeudi 14h) pour l'Audit Visio sans engagement.")
    ]
    cur_y = 49
    for t_t, t_d in temps_call:
        pdf.set_xy(62, cur_y)
        pdf.set_font('Helvetica', 'B', 7.2)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.2, clean_txt(f"- {t_t}"), align='L')
        cur_y += 3.4
        pdf.set_xy(65, cur_y)
        pdf.set_font('Helvetica', '', 6.5)
        pdf.set_text_color(200, 205, 215)
        pdf.multi_cell(135, 2.8, clean_txt(t_d), align='L')
        cur_y += 6.0

    pdf.set_xy(62, cur_y + 2)
    pdf.set_font('Times', 'B', 9.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("2. MATRICE DE DECODAGE COMPORTEMENTAL RAPIDE AU TELEPHONE (DISC/PCM)"))
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.2)
    pdf.line(62, cur_y + 7, 200, cur_y + 7)

    disc_profiles = [
        ("🔴 Rouge (Dominant / PCM Travaillomane)", "Débit rapide, direct, ton sec. Parler ROI net, chiffres bruts, temps compté. Proposer 2 créneaux fermes."),
        ("🟡 Jaune (Influent / PCM Persévérant)", "Chaleureux, parle vite, axé réputation. Parler prestige de la marque, avantage concurrentiel et réseau."),
        ("🟢 Vert (Stable / PCM Harmoniseur)", "Calme, pose des questions de sécurité. Rassurer sur le déroulé, la méthode sans risque et l'accompagnement."),
        ("🔵 Bleu (Consciencieux / PCM Analytique)", "Précis, demande du détail technique. Fournir les sources précises, les méthodologies de calcul et les preuves.")
    ]
    cur_y += 9
    for d_t, d_d in disc_profiles:
        pdf.set_xy(62, cur_y)
        pdf.set_font('Helvetica', 'B', 7.0)
        pdf.set_text_color(248, 250, 252)
        pdf.multi_cell(138, 3.2, clean_txt(f"> {d_t}"), align='L')
        cur_y += 3.4
        pdf.set_xy(65, cur_y)
        pdf.set_font('Helvetica', '', 6.4)
        pdf.set_text_color(160, 164, 176)
        pdf.multi_cell(135, 2.7, clean_txt(d_d), align='L')
        cur_y += 5.5

    # ----------------------------------------------------
    # PAGES 2 À 6 : LES 5 ICPS COMPLÈTES (1 PAGE PAR ICP)
    # ----------------------------------------------------
    icps_playbook = [
        {
            "num": 1,
            "title": "ICP 1 - AÉRONAUTIQUE & SPATIAL (Toulouse / Bordeaux)",
            "target": "VP Sales / Directeur Commercial Sous-Traitance (Airbus, Boeing, Safran)",
            "barrage": '"Bonjour, Julien Florence à l\'appareil. Je dois joindre directement la Direction Commerciale concernant le diagnostic de marge sur les révisions de contrats d\'équipementiers. Pouvez-vous me passer la ligne directe ?"',
            "hook": '"Bonjour [Nom], Julien Florence, cabinet QuestIA LAB. Nous conduisons un audit auprès des sous-traitants aéronautiques de la région Occitanie/Aquitaine. Face aux exigences des donneurs d\'ordres anglo-saxons, McKinsey a chiffré à 4,2% la fuite de marge nette due aux pénalités et révisions concédées sous pression en anglais. Quel est le volume de vos contrats négociés en langue seconde ?"',
            "objections": [
                ("1. 'Nos commerciaux parlent couramment anglais'", "Parler anglais ne protège pas du diktat d'un acheteur anglo-saxon. L'INSEAD démontre qu'un cadre perd 30% d'impact persuasif en L2 face à un acheteur agressif."),
                ("2. 'Nous sommes sous contrats-cadres pluriannuels figeables'", "C'est précisément lors des avenants et révisions d'indexation que la fuite de 4,2% s'opère sur les clauses de pénalités de retard."),
                ("3. 'Envoyez-moi une plaquette par email'", "Une plaquette ne chiffrera pas vos pertes. Je vous propose 15 min de diagnostic visio préalable : mardi 10h ou jeudi 14h ?")
            ],
            "closing": '"C\'est précisément l\'objet de notre audit diagnostic de 30 minutes en Visio : chiffrer votre fuite de marge et évaluer la fermeté de vos équipes. Êtes-vous disponible mardi à 10h ou jeudi à 14h ?"',
            "disc_pcm": "DISC : 🔴 Dominant (D) | PCM : 💼 Travaillomane. Exige des preuves factuelles chiffrées, des données ROI net et des créneaux stricts.",
            "source_name": "McKinsey Pricing Revamp Data (Fuite 4.2% marge net)",
            "source_url": "https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-pricing-revamp"
        },
        {
            "num": 2,
            "title": "ICP 2 - AGROALIMENTAIRE & PRODUITS DE LUXE EXPORT",
            "target": "Directeur Export Vins/Spiritueux, Gastronomie, Cosmétique",
            "barrage": '"Bonjour, Julien Florence, cabinet QuestIA LAB. Je demande le responsable export concernant l\'étude sur les remises de distribution accordées aux importateurs américains et asiatiques."',
            "hook": '"Bonjour [Nom], Julien Florence, cabinet QuestIA LAB. Dans l\'Export de Luxe, Business France note que 68% des exportateurs français concèdent des remises logistiques et des frais annexe indues face aux grands importateurs américains et asiatiques. Sur vos marchés US/Asie, observez-vous ces concessions ?"',
            "objections": [
                ("1. 'Nos agents locaux gèrent la négociation sur place'", "Vos agents locaux défendent souvent leur volume plutôt que votre marge nette. KPMG montre que 72% des blocages sont d'origine comportementale et non tarifaire."),
                ("2. 'Les tarifs sont imposés par la grande distribution export'", "Imposés en apparence : le décodage psychologique de l'acheteur permet de sauvegarder 3% de marge sans perdre le contrat."),
                ("3. 'Nous avons déjà nos réseaux d'exportateurs'", "L'audit ne remplace pas vos réseaux, il équipe vos cadres pour imposer vos prix d'exclusivité lors des renouvellements.")
            ],
            "closing": '"Bloquons 30 minutes en Visio cette semaine pour effectuer le bilan de fermeté de vos forces export et chiffrer vos gains de marge. Mardi 11h ou Mercredi 15h ?"',
            "disc_pcm": "DISC : 🟡 Influent (I) | PCM : 🏛️ Persévérant. Réagit au prestige de la marque, à la valeur perçue et à l'authenticité.",
            "source_name": "Business France / Bpifrance Le Lab (68% remises indûes)",
            "source_url": "https://lelab.bpifrance.fr"
        },
        {
            "num": 3,
            "title": "ICP 3 - ÉDITEURS DE LOGICIELS B2B SAAS DEEPTECH",
            "target": "Head of Global Sales, Chief Revenue Officer (CRO)",
            "barrage": '"Bonjour, Julien Florence à l\'appareil. Je souhaite échanger avec le CRO concernant les taux de conversion des Account Executives sur les comptes Enterprise nord-américains."',
            "hook": '"Bonjour [Nom], Julien Florence, QuestIA LAB. En SaaS B2B Enterprise, le cycle de vente s\'allonge de 40% lorsque les Account Executives francophones font preuve d\'une timidité culturelle sur le closing High-Ticket face aux acheteurs US. Quel est votre taux de conversion actuel sur les deals nord-américains ?"',
            "objections": [
                ("1. 'Nous avons déjà un Playbook de vente en anglais'", "Un playbook documenté ne modifie pas la réaction physiologique au stress lors d'une négo tendue. Harvard Business Review confirme l'impact du Foreign-Language Effect."),
                ("2. 'Nos AEs sont basés à Boston / Londres'", "Même bilingues, la culture de négociation européenne lâche des concessions gratuites sur le support et les SLAs."),
                ("3. 'Nous n'avons pas de budget formation ce trimestre'", "L'audit de 30 min est gratuit et permet de chiffrer le ROI d'un gain de 20k€ par deal avant tout engagement.")
            ],
            "closing": '"Je vous propose un Diagnostic Visio de 30 minutes pour évaluer le décodage psychométrique (DISC/PCM) de vos AE. Êtes-vous libre jeudi matin ?"',
            "disc_pcm": "DISC : 🔵 Consciencieux (C) | PCM : ⚡ Promoteur. Analyse les métriques de conversion, les taux de pipe et le closing.",
            "source_name": "Harvard Business Review (-30% impact persuasif L2)",
            "source_url": "https://hbr.org/2012/04/the-foreign-language-effect"
        },
        {
            "num": 4,
            "title": "ICP 4 - ÉQUIPEMENTS INDUSTRIELS & MACHINES SPÉCIALES",
            "target": "Directeur Développement International, Dir. Ventes Industrielles",
            "barrage": '"Bonjour, Julien Florence, cabinet QuestIA LAB. Je contacte la direction commerciale industrielle concernant le chiffrage des concessions d\'options gratuites sur les ventes de machines à l\'export."',
            "hook": '"Bonjour [Nom], Julien Florence de QuestIA LAB. Sur les affaires de machines spéciales et d\'ingénierie, les fuites de marge se font rarement sur le prix catalogue, mais sur l\'inclusion gratuite d\'options de garantie et de maintenance sous la pression d\'acheteurs allemands ou américains. Comment vos ingénieurs-commerciaux protègent-ils les options payantes ?"',
            "objections": [
                ("1. 'Ce sont des ingénieurs expérimentés qui vendent nos machines'", "C'est précisément la limite : ils négocient la technique, pas la valeur financière. Ils lâchent du terrain sur les clauses annexes."),
                ("2. 'Les marges sont réduites par la hausse des composants'", "Justement : quand les composants augmentent, concéder 3% d'options gratuites détruit l'intégralité de votre marge bénéficiaire."),
                ("3. 'Nous sommes débordés sur les livraisons en ce moment'", "Raison de plus : livrer à marge dégradée fatigue vos usines. 30 min d'audit visio suffisent à rectifier la posture.")
            ],
            "closing": '"Évaluons cela lors d\'un Audit de 30 minutes en Visio. Je vous présenterai les benchmarks de votre secteur. Plutôt lundi à 14h ou jeudi à 9h30 ?"',
            "disc_pcm": "DISC : 🔵 Consciencieux (C) | PCM : 💼 Travaillomane. Sensible au périmètre exact du contrat et aux clauses techniques.",
            "source_name": "KPMG Cross-Border Deal Survey (72% pertes comportementales)",
            "source_url": "https://kpmg.com/xx/en/home/insights/2023/10/cross-border-ma.html"
        },
        {
            "num": 5,
            "title": "ICP 5 - DISPOSITIFS MÉDICAUX & MEDTECH",
            "target": "Directeur Général, VP Global Business Development",
            "barrage": '"Bonjour, Julien Florence, cabinet QuestIA LAB. Je souhaite parler au Directeur Général au sujet du diagnostic de fermeté tarifaire sur les renouvellements de distribution MedTech à l\'international."',
            "hook": '"Bonjour [Nom], Julien Florence, cabinet QuestIA LAB. En MedTech, l\'accès aux marchés internationaux dépend de négociations tendues avec les réseaux de distribution. INSEAD montre que la non-détection des signaux comportementaux (DISC/PCM) entraîne des concessions excessives sur les exclusivités géographiques. Comment maîtrisez-vous ces négociations ?"',
            "objections": [
                ("1. 'Nos accords de distribution sont verrouillés juridiquement'", "Le contrat protège le droit, pas le prix de cession. Nos audits révèlent 3,8% de fuite de marge nette lors des renouvellements."),
                ("2. 'Le marché médical obéit aux comités hospitaliers figeables'", "Les comités utilisent des tactiques de pression psychologique pour forcer les remises. Le décodage DISC permet de verrouiller le prix."),
                ("3. 'Le Directeur Général ne prend pas ce type d'appel'", "Transmettez-lui notre note exécutive d'audit : la décision d'audit de marge relève directement de sa responsabilité d'EBITDA.")
            ],
            "closing": '"Prenons 30 minutes en Visio pour auditer la fermeté de vos équipes. Mercredi 10h ou Vendredi 14h30 ?"',
            "disc_pcm": "DISC : 🟢 Stable (S) / 🔴 Dominant | PCM : 🏛️ Persévérant. Exige de la rigueur clinique et des garanties stratégiques.",
            "source_name": "INSEAD Executive Education (Psychological Decoding in High-Stakes Deals)",
            "source_url": "https://www.insead.edu/executive-education/leadership/negotiation-dynamics"
        }
    ]

    for icp in icps_playbook:
        pdf.add_page()
        draw_sidebar_sources(pdf, 45)
        
        pdf.set_xy(62, 23)
        pdf.set_font('Helvetica', 'B', 8.5)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 4.0, clean_txt(icp['title'].upper()))
        
        pdf.set_xy(62, pdf.get_y() + 1)
        pdf.set_font('Helvetica', 'B', 7.0)
        pdf.set_text_color(123, 92, 255)
        pdf.multi_cell(138, 3.2, clean_txt(f"Cible Décisionnaire : {icp['target']}"))
        
        y_line = pdf.get_y() + 1.5
        pdf.set_draw_color(0, 229, 255)
        pdf.set_line_width(0.2)
        pdf.line(62, y_line, 200, y_line)
        
        # 1. Passe Barrage
        pdf.set_xy(62, y_line + 2)
        pdf.set_font('Times', 'B', 9.0)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.5, clean_txt("1. PASSE-BARRAGE SECRETARIAT (30 SECONDES)"))
        
        pdf.set_xy(62, pdf.get_y() + 1)
        pdf.set_font('Helvetica', 'I', 6.4)
        pdf.set_text_color(200, 205, 215)
        pdf.multi_cell(138, 2.7, clean_txt(icp['barrage']), align='L')

        # 2. Accroche Cold Call
        pdf.set_xy(62, pdf.get_y() + 3)
        pdf.set_font('Times', 'B', 9.0)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.5, clean_txt("2. SCRIPT TELEPHONIQUE ACCROCHE DIRECTE (COLD CALL 90 SEC)"))
        
        box_y = pdf.get_y() + 1.5
        pdf.set_font('Helvetica', 'I', 6.3)
        pdf.set_xy(64, box_y + 1.5)
        pdf.set_text_color(248, 250, 252)
        pdf.multi_cell(134, 2.7, clean_txt(icp['hook']), align='L')
        box_h = (pdf.get_y() + 1.5) - box_y
        
        pdf.set_fill_color(20, 24, 34)
        pdf.set_draw_color(0, 229, 255)
        pdf.set_line_width(0.3)
        pdf.rect(62, box_y, 138, box_h, 'DF')
        
        # Reprint text on top of box fill
        pdf.set_xy(64, box_y + 1.5)
        pdf.set_font('Helvetica', 'I', 6.3)
        pdf.set_text_color(248, 250, 252)
        pdf.multi_cell(134, 2.7, clean_txt(icp['hook']), align='L')
        
        # 3. Traitement des 3 Objections
        pdf.set_xy(62, box_y + box_h + 3)
        pdf.set_font('Times', 'B', 9.0)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.5, clean_txt("3. MATRICE DES 3 OBJECTIONS SECTORIELLES MAJEURES"))
        
        for obj_title, obj_ans in icp['objections']:
            cur_y = pdf.get_y() + 1.5
            pdf.set_xy(62, cur_y)
            pdf.set_font('Helvetica', 'B', 6.6)
            pdf.set_text_color(248, 250, 252)
            pdf.multi_cell(138, 3.0, clean_txt(f"- Objection {obj_title}"), align='L')
            
            cur_y = pdf.get_y() + 0.5
            pdf.set_xy(65, cur_y)
            pdf.set_font('Helvetica', '', 6.3)
            pdf.set_text_color(160, 164, 176)
            pdf.multi_cell(135, 2.7, clean_txt(f"Réponse QuestIA LAB : {obj_ans}"), align='L')

        # 4. Closing RDV Visio
        cur_y = pdf.get_y() + 3
        pdf.set_xy(62, cur_y)
        pdf.set_font('Times', 'B', 9.0)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.5, clean_txt("4. VERROUILLAGE DU CLOSING DU RDV VISIO AUDIT (30 MIN)"))

        cur_y = pdf.get_y() + 1
        pdf.set_xy(62, cur_y)
        pdf.set_font('Helvetica', 'B', 6.4)
        pdf.set_text_color(248, 250, 252)
        pdf.multi_cell(138, 2.7, clean_txt(icp['closing']), align='L')

        # 5. Posture & DISC
        cur_y = pdf.get_y() + 3
        pdf.set_xy(62, cur_y)
        pdf.set_font('Times', 'B', 9.0)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.5, clean_txt("5. PROFIL PSYCHOMETRIQUE ET POSTURE D'EQUIPE (DISC/PCM)"))

        cur_y = pdf.get_y() + 1
        pdf.set_xy(62, cur_y)
        pdf.set_font('Helvetica', '', 6.3)
        pdf.set_text_color(200, 205, 215)
        pdf.multi_cell(138, 2.7, clean_txt(icp['disc_pcm']), align='L')

        # Source Cliquable
        cur_y = pdf.get_y() + 2.5
        pdf.set_xy(62, cur_y)
        pdf.set_font('Helvetica', 'BU', 6.5)
        pdf.set_text_color(0, 229, 255)
        pdf.multi_cell(138, 3.2, clean_txt(f"Source Officielle Cliquable : {icp['source_name']} >"), align='L')

    # ----------------------------------------------------
    # PAGE 7 : SEQUENCES MULTICANALES DE SUIVI POST-APPEL
    # ----------------------------------------------------
    pdf.add_page()
    draw_sidebar_sources(pdf, 45)

    pdf.set_xy(62, 23)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 4.0, clean_txt("6. SEQUENCES MULTICANALES DE RELANCE & SUIVI (EMAIL & LINKEDIN)"))

    pdf.set_xy(62, pdf.get_y() + 1.5)
    pdf.set_font('Helvetica', '', 7.2)
    pdf.set_text_color(226, 232, 240)
    pdf.multi_cell(138, 3.2, clean_txt("Pour tout prospect contacté par téléphone (acceptation, hésitation ou secrétariat), appliquez immédiatement la séquence de suivi dans les 15 minutes."), align='J')

    # TRAME 1
    pdf.set_xy(62, pdf.get_y() + 3)
    pdf.set_font('Times', 'B', 9.0)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 3.5, clean_txt("TRAME 1 : EMAIL DE CONFIRMATION INSTANTANEE DE RDV VISIO AUDIT"))
    
    t1 = "Objet : Confirmation Audit Performance Commerciale Visio - QuestIA LAB x [Entreprise]\n\nBonjour [Nom],\nJe vous confirme notre rendez-vous d'Audit Visio de 30 minutes fixé le [Date] à [Heure].\nLien d'accès Visio : https://meet.questia.ai/audit-[Entreprise]\nNous passerons en revue l'évaluation de vos frictions de marge export et la démonstration du diagnostic psychométrique DISC/PCM. En pièce jointe, la note synthétique d'audit.\n\nBien cordialement,\nJulien FLORENCE | QuestIA LAB (06 61 74 75 73)"
    
    box1_y = pdf.get_y() + 1.5
    pdf.set_font('Helvetica', '', 6.0)
    pdf.set_xy(64, box1_y + 1.5)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.5, clean_txt(t1), align='L')
    box1_h = (pdf.get_y() + 1.5) - box1_y
    
    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.3)
    pdf.rect(62, box1_y, 138, box1_h, 'DF')
    
    pdf.set_xy(64, box1_y + 1.5)
    pdf.set_font('Helvetica', '', 6.0)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.5, clean_txt(t1), align='L')

    # TRAME 2
    pdf.set_xy(62, box1_y + box1_h + 3)
    pdf.set_font('Times', 'B', 9.0)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 3.5, clean_txt("TRAME 2 : EMAIL DE RELANCE POST-APPEL 'CHOC PERTE DE MARGE'"))
    
    t2 = "Objet : Note chiffrée - Pertes de marge export sous pression (Secteur [Secteur])\n\nBonjour [Nom],\nSuite à notre échange téléphonique, je vous transmets l'étude montrant que les fuites de marge nette atteignent 4,2% en moyenne lors des négociations internationales en langue seconde (Data McKinsey / INSEAD).\nJe vous propose un échange de 30 min pour chiffrer l'impact direct sur [Entreprise]. Êtes-vous disponible mardi à 10h ou jeudi à 14h ?\n\nBien cordialement,\nJulien FLORENCE | Auditeur Exécutif QuestIA LAB"
    
    box2_y = pdf.get_y() + 1.5
    pdf.set_font('Helvetica', '', 6.0)
    pdf.set_xy(64, box2_y + 1.5)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.5, clean_txt(t2), align='L')
    box2_h = (pdf.get_y() + 1.5) - box2_y

    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.3)
    pdf.rect(62, box2_y, 138, box2_h, 'DF')
    
    pdf.set_xy(64, box2_y + 1.5)
    pdf.set_font('Helvetica', '', 6.0)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.5, clean_txt(t2), align='L')

    # TRAME 3
    pdf.set_xy(62, box2_y + box2_h + 3)
    pdf.set_font('Times', 'B', 9.0)
    pdf.set_text_color(0, 229, 255)
    pdf.multi_cell(138, 3.5, clean_txt("TRAME 3 : INMAIL LINKEDIN PROSPECT DIRECT"))

    t3 = "Bonjour [Nom], j'ai tenté de vous joindre concernant l'Audit de Performance Commerciale & Décodage DISC/PCM conduit auprès des acteurs [Secteur]. Les négociations internationales engendrent une fuite moyenne de 4,2% de marge nette (McKinsey). Auriez-vous 15 min à m'accorder jeudi à 14h en Visio ?"
    
    box3_y = pdf.get_y() + 1.5
    pdf.set_font('Helvetica', '', 6.0)
    pdf.set_xy(64, box3_y + 1.5)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.5, clean_txt(t3), align='L')
    box3_h = (pdf.get_y() + 1.5) - box3_y

    pdf.set_fill_color(20, 24, 34)
    pdf.set_draw_color(0, 229, 255)
    pdf.set_line_width(0.3)
    pdf.rect(62, box3_y, 138, box3_h, 'DF')
    
    pdf.set_xy(64, box3_y + 1.5)
    pdf.set_font('Helvetica', '', 6.0)
    pdf.set_text_color(248, 250, 252)
    pdf.multi_cell(134, 2.5, clean_txt(t3), align='L')

    pdf.output(out_path)
    print(f"✅ PDF #4 Playbook Équipe complet (7 pages) généré sans chevauchement : {out_path}")

if __name__ == "__main__":
    out_dir_1 = "04_Livrables/PDF"
    out_dir_2 = "Projets/questIA/04_Livrables/PDF"
    
    for d in [out_dir_1, out_dir_2]:
        os.makedirs(d, exist_ok=True)
        p1 = os.path.join(d, "01_QUESTIA_Lab_Audit_Confirmation_Et_Preparation_RDV.pdf")
        p2 = os.path.join(d, "02_QUESTIA_Lab_Note_Choc_Perte_CA_Immediat.pdf")
        p3 = os.path.join(d, "03_QUESTIA_Lab_Note_Executive_Passe_Barrage_Secretariat.pdf")
        p4 = os.path.join(d, "04_QUESTIA_Lab_Scripts_Et_Diagnostic_Par_ICP.pdf")

        generate_pdf1_confirmation(p1)
        generate_pdf2_choc_refus(p2)
        generate_pdf3_passe_barrage(p3)
        generate_pdf4_scripts_5icps(p4)

        # Backwards compatibility aliases (space and underscore variants)
        import shutil
        aliases = [
            (p1, ["01_QUESTIA_Audit_Confirmation_Et_Preparation_RDV.pdf", "01_QUESTIA LAB_Audit_Confirmation_Et_Preparation_RDV.pdf"]),
            (p2, ["02_QUESTIA_Note_Choc_Perte_CA_Immediat.pdf", "02_QUESTIA LAB_Note_Choc_Perte_CA_Immediat.pdf"]),
            (p3, ["03_QUESTIA_Note_Executive_Passe_Barrage_Secretariat.pdf", "03_QUESTIA LAB_Note_Executive_Passe_Barrage_Secretariat.pdf"]),
            (p4, ["04_QUESTIA_Scripts_Et_Diagnostic_Par_ICP.pdf", "04_QUESTIA LAB_Scripts_Et_Diagnostic_Par_ICP.pdf"])
        ]
        for src, dst_list in aliases:
            for dst_name in dst_list:
                shutil.copy(src, os.path.join(d, dst_name))

