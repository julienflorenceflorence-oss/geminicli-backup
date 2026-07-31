#!/usr/bin/env python3
"""
Générateur de PDF au Graphisme Sombre & Or (Identique à la charte CV de Julien Florence)
Thème: Fond Sombre (#0F1117), Sidebar (#141822), Titres Or Metallic (#D4AF37), Texte Blanc/Gris (#F8FAFC)
"""

import sys
import os
sys.path.insert(0, '/Users/admin/Library/Python/3.9/lib/python/site-packages')
from fpdf import FPDF

class DarkGoldPDF(FPDF):
    def __init__(self, title_text="DOCUMENT EXECUTION", subtitle_text="JULIEN FLORENCE"):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.title_text = title_text
        self.subtitle_text = subtitle_text
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        # Background page entière (Sombre #0F1117)
        self.set_fill_color(15, 17, 23)
        self.rect(0, 0, 210, 297, 'F')
        
        # Sidebar gauche (Gris Sombre #141822)
        self.set_fill_color(20, 24, 34)
        self.rect(0, 0, 60, 297, 'F')
        
        # Ligne verticale de séparation Or
        self.set_draw_color(212, 175, 55)
        self.set_line_width(0.4)
        self.line(60, 0, 60, 297)

        # En-tête Sidebar
        self.set_xy(5, 12)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(212, 175, 55) # Gold
        self.cell(50, 6, "JULIEN FLORENCE", align='C')
        
        self.set_xy(5, 18)
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(148, 163, 184) # Muted
        self.cell(50, 4, "DIRECTEUR HOTELLERIE & F&B", align='C')
        
        self.set_xy(5, 23)
        self.set_draw_color(212, 175, 55)
        self.line(10, 25, 50, 25)

        # En-tête Main Content
        self.set_xy(68, 12)
        self.set_font('Times', 'B', 14)
        self.set_text_color(212, 175, 55) # Gold Serif
        self.cell(130, 7, self.title_text, align='L')
        
        self.set_xy(68, 19)
        self.set_font('Helvetica', 'B', 8.5)
        self.set_text_color(248, 250, 252) # White
        self.cell(130, 5, self.subtitle_text, align='L')
        
        self.set_draw_color(212, 175, 55)
        self.set_line_width(0.5)
        self.line(68, 26, 200, 26)
        self.ln(10)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(148, 163, 184)
        self.set_x(68)
        self.cell(130, 6, f"JOST Hotel Bordeaux Gare | Page {self.page_no()}", align='R')

def draw_sidebar_section(pdf, y_start, title, items):
    pdf.set_xy(5, y_start)
    pdf.set_font('Times', 'B', 9)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(50, 5, title.upper(), align='L')
    
    pdf.set_draw_color(212, 175, 55)
    pdf.set_line_width(0.2)
    pdf.line(5, pdf.get_y() + 5, 55, pdf.get_y() + 5)
    pdf.set_xy(5, pdf.get_y() + 7)
    
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    for item in items:
        pdf.set_x(5)
        pdf.multi_cell(50, 3.8, f"> {item}")
        pdf.ln(1)

def clean_txt(text):
    return text.replace("—", "-").replace("’", "'").replace("°", "o").replace("€", "EUR").replace("…", "...").replace("«", '"').replace("»", '"').replace("œ", "oe").replace("Œ", "OE")

def build_cover_letter_pdf(out_path):
    pdf = DarkGoldPDF("LETTRE DE MOTIVATION & MATRICE", "CANDIDATURE DIRECTEUR HÔTEL - JOST BORDEAUX")
    pdf.add_page()
    
    # Sidebar
    draw_sidebar_section(pdf, 32, "Candidat", [
        "Julien FLORENCE",
        "Mobilite : Bordeaux & Gironde",
        "Experience : 15 ans CHR & Luxe",
        "Diplome : Management Digital",
        "Posture : ENTJ-A (94% Org.)"
    ])
    
    draw_sidebar_section(pdf, 85, "Expertises Cles", [
        "Pilotage P&L & Ratios F&B",
        "Leadership Sportif (Coach)",
        "Acquisition Social Media",
        "Management 30 Salaries",
        "Standards Luxe & CS"
    ])
    
    draw_sidebar_section(pdf, 135, "Contacts", [
        "Tel : 06 61 74 75 73",
        "Email : julien.florence@email.com",
        "LinkedIn : Julien Florence",
        "Zone : Bordeaux Gare"
    ])
    
    # Main Content
    pdf.set_xy(68, 32)
    
    # Subject Box
    pdf.set_fill_color(28, 34, 48)
    pdf.set_draw_color(212, 175, 55)
    pdf.rect(68, 32, 132, 10, 'DF')
    pdf.set_xy(70, 33)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(128, 8, clean_txt("Objet : Candidature Directeur d'Hotel - Alignement JOST Bordeaux"))
    
    pdf.set_xy(68, 46)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, "MATRICE DE CORRELATION (BESOINS VS ATOUTS)")
    pdf.set_draw_color(212, 175, 55)
    pdf.line(68, 52, 200, 52)
    pdf.set_xy(68, 54)
    
    # Table Header
    pdf.set_fill_color(20, 24, 34)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(40, 5, " Exigence JOST", 1, 0, 'L', True)
    pdf.cell(42, 5, " Atout Julien Florence", 1, 0, 'L', True)
    pdf.cell(50, 5, " Preuve d'Impact", 1, 1, 'L', True)
    
    matrix_data = [
        ("P&L & CA +140%", "Ma Salle a Manger (Paris 1er)", "Partenariats galeries art, EVG/EVJF & Tour Op."),
        ("Rigueur F&B Luxe", "Au Clos (Angl.) & Sommelier", "Soirees Fooding, œnologie & controle Bev Cost"),
        ("Hôtellerie Palace 5*", "Guanahani (St-Barth LHW)", "Management du Room Service haut de gamme"),
        ("Conseil Hôtelier 360", "1 an d'Accompagnement B2B", "Audit châteaux, hôtels, gîtes, chambres d'hôtes")
    ]
    
    pdf.set_font('Helvetica', '', 7)
    pdf.set_text_color(226, 232, 240)
    for req, atout, preuve in matrix_data:
        pdf.set_x(68)
        pdf.cell(38, 4.5, clean_txt(f" {req}"), 1, 0, 'L')
        pdf.cell(46, 4.5, clean_txt(f" {atout}"), 1, 0, 'L')
        pdf.cell(48, 4.5, clean_txt(f" {preuve}"), 1, 1, 'L')
        
    pdf.ln(4)
    pdf.set_x(68)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, "LETTRE DE MOTIVATION OFFICIELLE (PREUVES FACTUELLES)")
    pdf.line(68, pdf.get_y() + 5, 200, pdf.get_y() + 5)
    pdf.set_xy(68, pdf.get_y() + 7)
    
    letter_paragraphs = [
        "Messieurs les Dirigeants,",
        "Votre annonce pour JOST Hotel Bordeaux pose une exigence claire : un profil uniquement hôtelier n'est pas recherche. Developper un hotspot hybride exige l'energie d'un entrepreneur de restauration, la rigueur d'un gestionnaire de P&L, l'agilite d'un animateur de lieu et une vraie connaissance hoteliere.",
        "C'est la somme factuelle de mes experiences passees qui fait de moi un candidat incontestable :",
        "1. Pilotage P&L & Croissance F&B (+140% de CA en 5 ans) : En tant que Directeur de restaurant (Ma Salle a Manger, Paris 1er), j'ai pilote le P&L et fait progresser le CA de +140% en 5 ans via l'etude d'environnement, partenariats galeries d'art, evenements (EVG/EVJF, mariages) et Tour Operateurs. Une capacite directe a booster votre pole Solia et rooftop JOST On Top.",
        "2. Rigueur F&B International & Evenementiel Fooding : Mon parcours en Angleterre (Au Clos / Relais & Chateaux) et mon poste de Manager Sommelier m'ont apporte la maitrise des couts matiere (Bev Cost) et l'animation de soirees Fooding et evenements oenologiques.",
        "3. Culture Hoteliere d'Excellence & Vision 360o : Au Guanahani (Palace 5* St-Barth LHW), j'ai manage le Room Service d'exception. De plus, j'ai passe 1 an a accompagner des hoteliers de tous formats (chateaux, grands gites, hotels, chambres d'hotes, commercants). Je connais leurs problematiques de couts fixes et la realite du terrain.",
        "4. Leadership Agile (Coach Handball) : Piloter 30 collaborateurs exige l'agilite de mon parcours de coach (briefs agiles, temps morts, sang-froid en coup de feu) pour maintenir la satisfaction > 8.5/10.",
        "Je serais honore de vous presenter mon Plan d'Action a 90 Jours lors d'un entretien.",
        "Julien FLORENCE - Bordeaux"
    ]
    
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(248, 250, 252)
    for p in letter_paragraphs:
        pdf.set_x(68)
        pdf.multi_cell(132, 3.6, clean_txt(p))
        pdf.ln(1.5)
        
    pdf.output(out_path)
    print(f"✅ PDF généré : {out_path}")

def build_pl_pdf(out_path):
    pdf = DarkGoldPDF("SIMULATION P&L & RATIOS DE GESTION", "MODELE FINANCIER JOST HOTEL BORDEAUX (96 CLES)")
    pdf.add_page()
    
    # Sidebar
    draw_sidebar_section(pdf, 32, "Structure P&L", [
        "CA Estime : 3.20 M EUR",
        "Nuitees : 50% du CA",
        "F&B Resto : 25% du CA",
        "Rooftop Bar : 20% du CA",
        "MICE/Evenements : 5%"
    ])
    
    draw_sidebar_section(pdf, 85, "Targets Marge", [
        "EBITDA Target : 35.5%",
        "Prime Cost : < 60%",
        "Food Cost : 28% - 32%",
        "Beverage Cost : 18% - 22%",
        "Masse Salariale : 32%"
    ])
    
    # Main Content
    pdf.set_xy(68, 32)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, "COMPTE DE RESULTAT PREVISIONNEL (P&L ANNUEL)")
    pdf.set_draw_color(212, 175, 55)
    pdf.line(68, 38, 200, 38)
    pdf.set_xy(68, 40)
    
    lines = [
        ("CHIFFRE D'AFFAIRES TOTAL", "3 200 000 EUR", "100.0%", True),
        ("  1. Nuitees (Chambres & Dortoirs)", "1 600 000 EUR", "50.0%", False),
        ("  2. Restauration (Nonna Gioia / Solia)", "800 000 EUR", "25.0%", False),
        ("  3. Bar & Rooftop (JOST On Top)", "640 000 EUR", "20.0%", False),
        ("  4. Evenementiel & MICE (Lieu Cheri)", "160 000 EUR", "5.0%", False),
        ("CHARGES VARIABLES & COUTS DIRECTS", "- 720 000 EUR", "-22.5%", True),
        ("  . Cout Matiere F&B (Food/Bev Cost)", "- 432 000 EUR", "30% F&B", False),
        ("  . Commissions OTAs & Shotgun", "- 160 000 EUR", "5.0%", False),
        ("  . Produits d'accueil, buanderie", "- 128 000 EUR", "4.0%", False),
        ("MASSE SALARIALE (Personnel 30 ETP)", "- 1 024 000 EUR", "-32.0%", True),
        ("FRAIS GENERAUX & OPEX (Energie...)", "- 320 000 EUR", "-10.0%", True),
        ("MARGE D'EBITDA / GOP (RESULTAT NET)", "1 136 000 EUR", "35.5%", True)
    ]
    
    for label, val, pct, is_bold in lines:
        pdf.set_x(68)
        if is_bold:
            pdf.set_fill_color(28, 34, 48)
            pdf.set_font('Helvetica', 'B', 7.5)
            pdf.set_text_color(212, 175, 55)
        else:
            pdf.set_fill_color(20, 24, 34)
            pdf.set_font('Helvetica', '', 7)
            pdf.set_text_color(226, 232, 240)
            
        pdf.cell(75, 4.5, clean_txt(f" {label}"), 1, 0, 'L', True)
        pdf.cell(32, 4.5, clean_txt(f"{val} "), 1, 0, 'R', True)
        pdf.cell(25, 4.5, clean_txt(f"{pct} "), 1, 1, 'R', True)
        
    pdf.ln(5)
    pdf.set_x(68)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, "FORMULES FINANCIERES & RATIOS DE GESTION")
    pdf.line(68, pdf.get_y() + 5, 200, pdf.get_y() + 5)
    pdf.set_xy(68, pdf.get_y() + 7)
    
    ratios = [
        ("RevPAR", "CA Nuitees / Chambres Disponibles", "Boussole performance nuitees"),
        ("Food Cost %", "(Achats Nourriture / CA Nourriture) x 100", "Target : 28% a 32%"),
        ("Beverage Cost %", "(Achats Boissons / CA Boissons) x 100", "Target : 18% a 22% (Marge Bar)"),
        ("Prime Cost %", "(Cout Matiere + Masse Salariale) / CA", "Target : < 60% (Sante globale)"),
        ("Marge EBITDA %", "(EBITDA / CA Total) x 100", "Target Hybride : 30% a 38%")
    ]
    
    for r_name, r_form, r_desc in ratios:
        pdf.set_x(68)
        pdf.set_font('Helvetica', 'B', 7.5)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(30, 4, clean_txt(f"> {r_name} :"), 0, 0, 'L')
        pdf.set_font('Helvetica', '', 7)
        pdf.set_text_color(248, 250, 252)
        pdf.cell(100, 4, clean_txt(f"{r_form} - {r_desc}"), 0, 1, 'L')

    pdf.output(out_path)
    print(f"✅ PDF généré : {out_path}")

def build_questions_pdf(out_path):
    pdf = DarkGoldPDF("GUIDE 5 QUESTIONS FINANCIERES PIEGES", "PREPARATION ENTRETIEN ALBAN RUGGIERO (EX-ACCOR)")
    pdf.add_page()
    
    # Sidebar
    draw_sidebar_section(pdf, 32, "Profil Recruteur", [
        "Alban RUGGIERO",
        "CEO MELT Group",
        "Diplome : Mines",
        "Ex-Cadre Groupe Accor",
        "Profil : P&L Operator"
    ])
    
    draw_sidebar_section(pdf, 85, "Objectifs Guide", [
        "Repondre avec rigueur",
        "Eviter les pieges panique",
        "Demonter la maitrise P&L",
        "Valoriser le RevPAG",
        "Affirmer les 3 KPIs matin"
    ])
    
    pdf.set_xy(68, 32)
    
    q_data = [
        ("Q1 : Food Cost a 36% en ete sur le Rooftop ?",
         "Reagir en augmentant les prix tout de suite.",
         "Rechercher la cause racine (sur-dosage bar, casse). Inventaire hebdo des bouteilles, fiches techniques strictes, et promotion des cocktails signatures a fort Beverage Cost."),
        
        ("Q2 : Dortoir a 35 EUR vs Chambre Signature a 120 EUR ?",
         "Penser que la chambre est toujours plus rentable.",
         "Raisonner en RevPAG (CA total par client). Le week-end, un dortoir de 8 lits a 35 EUR fait 280 EUR + 8x20 EUR de cocktails rooftop. Le dortoir degage un CA global superieur."),
        
        ("Q3 : Masse salariale a 35% du CA en hiver ?",
         "Supprimer des postes au hasard et degrader le service.",
         "Polyvalence Flextime : mensualiser les heures et polycompetence reception/bar aux heures creuses (14h-17h). Digitaliser tout en sanctuarisant la presence aux pics 18h-22h."),
        
        ("Q4 : Chute de l'EBITDA de 4 pts malgre un CA en hausse ?",
         "Accuser l'energie ou le marche sans analyser le Prime Cost.",
         "Degradation du Prime Cost (<60%) ou hausse commissions. Verifier 3 points : ratio reservations directes vs OTAs/Shotgun, heures supp F&B et gaspillage cuisine."),
        
        ("Q5 : Vos 3 indicateurs financiers du matin a 8h30 ?",
         "Repondre des generalites vagues (ex: le CA d'hier).",
         "1. RevPAR de la veille vs budget/N-1. 2. Prime Cost F&B cumule du mois. 3. Taux de captage F&B (% clients heberges consommant au bar/resto).")
    ]
    
    for title, trap, ans in q_data:
        pdf.set_x(68)
        pdf.set_font('Helvetica', 'B', 8)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(132, 4.5, clean_txt(title))
        pdf.set_xy(68, pdf.get_y() + 4.5)
        
        pdf.set_font('Helvetica', 'I', 7)
        pdf.set_text_color(248, 113, 113) # Red light
        pdf.multi_cell(132, 3.5, clean_txt(f"X Piege : {trap}"))
        
        pdf.set_x(68)
        pdf.set_font('Helvetica', '', 7)
        pdf.set_text_color(226, 232, 240)
        pdf.multi_cell(132, 3.5, clean_txt(f"V Reponse d'Elite : {ans}"))
        pdf.ln(2.5)

    pdf.output(out_path)
    print(f"✅ PDF généré : {out_path}")

def build_prices_pdf(out_path):
    pdf = DarkGoldPDF("GRILLE TARIFAIRE & RESUME DES PRIX", "JOST HOTEL BORDEAUX (HEBERGEMENT, F&B & SALAIRE)")
    pdf.add_page()
    
    # Sidebar
    draw_sidebar_section(pdf, 32, "Categories", [
        "Hebergement (96 cles)",
        "Trattoria Nonna Gioia",
        "Rooftop JOST On Top",
        "MICE Lieu Cheri",
        "Package Directeur"
    ])
    
    pdf.set_xy(68, 32)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, "1. TARIFS HEBERGEMENT & NUITEES")
    pdf.set_draw_color(212, 175, 55)
    pdf.line(68, 38, 200, 38)
    pdf.set_xy(68, 40)
    
    h_data = [
        ("Lit en Dortoir Partage", "Rideau, casier securise", "21 EUR - 45 EUR / lit"),
        ("Dortoir Privatise", "Dortoir 4 a 8 personnes", "140 EUR - 280 EUR"),
        ("Chambre Signature", "Double Confort (15-18 m2)", "85 EUR - 160 EUR"),
        ("Chambre Oversize", "Familiale (30 m2 - 4 pers.)", "140 EUR - 240 EUR"),
        ("Suite / Appartement", "Logement autonome complet", "180 EUR - 320 EUR")
    ]
    
    for item, desc, price in h_data:
        pdf.set_x(68)
        pdf.set_font('Helvetica', 'B', 7)
        pdf.set_text_color(226, 232, 240)
        pdf.cell(45, 4.2, clean_txt(f" {item}"), 1, 0, 'L')
        pdf.set_font('Helvetica', '', 6.8)
        pdf.cell(52, 4.2, clean_txt(f" {desc}"), 1, 0, 'L')
        pdf.set_font('Helvetica', 'B', 7)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(35, 4.2, clean_txt(f"{price} "), 1, 1, 'R')
        
    pdf.ln(4)
    pdf.set_x(68)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, "2. RESTAURATION, ROOFTOP & SALAIRE DIRECTEUR")
    pdf.line(68, pdf.get_y() + 5, 200, pdf.get_y() + 5)
    pdf.set_xy(68, pdf.get_y() + 7)
    
    f_data = [
        ("Formule Midi Solia", "Entree+Plat ou Plat+Dessert", "17 EUR - 21 EUR"),
        ("Plats de Partage / Pastas", "Cuisine italienne & World", "14 EUR - 24 EUR"),
        ("Pool Party Brunch", "Dimanche Rooftop + Piscine", "29 EUR - 36 EUR / pers"),
        ("Cocktails Signatures", "Creations JOST On Top", "12 EUR - 16 EUR"),
        ("Pass Soiree Shotgun", "Entree Pool Party + Conso", "10 EUR - 20 EUR"),
        ("Coworking Lieu Cheri", "Pass Journee + cafe/wifi", "15 EUR - 25 EUR / jour"),
        ("Seminaire Journee", "Salle + pauses + dejeuner", "65 EUR - 95 EUR / pers"),
        ("Fixe Directeur (CDI)", "Salaire fixe brut annuel", "50k EUR - 60k EUR / an"),
        ("Variable Directeur", "Prime objectifs EBITDA/TO", "5k EUR - 10k EUR / an")
    ]
    
    for item, desc, price in f_data:
        pdf.set_x(68)
        pdf.set_font('Helvetica', 'B', 7)
        pdf.set_text_color(226, 232, 240)
        pdf.cell(45, 4.2, clean_txt(f" {item}"), 1, 0, 'L')
        pdf.set_font('Helvetica', '', 6.8)
        pdf.cell(52, 4.2, clean_txt(f" {desc}"), 1, 0, 'L')
        pdf.set_font('Helvetica', 'B', 7)
        pdf.set_text_color(212, 175, 55)
        pdf.cell(35, 4.2, clean_txt(f"{price} "), 1, 1, 'R')

    pdf.output(out_path)
    print(f"✅ PDF généré : {out_path}")

def build_strategic_post_pdf(out_path):
    pdf = DarkGoldPDF("ANALYSE STRATÉGIQUE DES POSTS & ACTUS", "ENJEUX CLÉS MELT GROUP / JOST HÔTEL BORDEAUX")
    pdf.add_page()
    
    # Sidebar
    draw_sidebar_section(pdf, 32, "Enjeux Clés", [
        "Virage MICE B2B",
        "Partenariat Doyield",
        "Revenue Management",
        "Gare Saint-Jean",
        "Baisse com. OTAs"
    ])
    
    pdf.set_xy(68, 32)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, clean_txt("1. LE VIRAGE STRATEGIQUE MICE & EVENEMENTIEL B2B"))
    pdf.set_draw_color(212, 175, 55)
    pdf.line(68, 38, 200, 38)
    pdf.set_xy(68, 40)
    
    p1 = [
        "Podcast Event Shake #90 & Posts Alban Ruggiero / Damien Ferrieres :",
        "La direction de MELT Group a formalise un pivot majeur : faire du MICE (seminaires, afterworks d'entreprises, conventions) le relais de croissance N o1 du groupe.",
        "Enjeu JOST Bordeaux : Transformer le Lieu Cheri et le Rooftop en espaces d'affaires privatisables du lundi au jeudi pour les 50 grands comptes du quartier Amédee St-Germain."
    ]
    
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    for p in p1:
        pdf.set_x(68)
        pdf.multi_cell(132, 3.6, clean_txt(p))
        pdf.ln(1.5)
        
    pdf.ln(3)
    pdf.set_x(68)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, clean_txt("2. PARTENARIAT REVENUE MANAGEMENT DOYIELD"))
    pdf.line(68, pdf.get_y() + 5, 200, pdf.get_y() + 5)
    pdf.set_xy(68, pdf.get_y() + 7)
    
    p2 = [
        "Annonce Officielle MELT Group x Doyield :",
        "MELT Group s'est associe a Doyield pour automatiser le Revenue Management et booster la reservation directe sur l'ensemble de ses 4 hotels (Bordeaux, Montpellier, Le Havre, Lille).",
        "Enjeu JOST Bordeaux : Arbitrage dynamique des lits en dortoir vs chambres Signature selon le calendrier bordelais, et reduction directe des commissions versees a Booking/Airbnb."
    ]
    
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    for p in p2:
        pdf.set_x(68)
        pdf.multi_cell(132, 3.6, clean_txt(p))
        pdf.ln(1.5)

    pdf.output(out_path)
    print(f"✅ PDF généré : {out_path}")

def build_power_bi_pdf(out_path):
    pdf = DarkGoldPDF("GUIDE D'EXCELLENCE POWER BI", "ANALYSE STRATÉGIQUE, DAX & CAS D'USAGE MÉTIER")
    pdf.add_page()
    
    # Sidebar
    draw_sidebar_section(pdf, 32, "Composants BI", [
        "Power BI Desktop",
        "Power BI Service",
        "Power BI Mobile",
        "Power Query (M)",
        "Langage DAX",
        "Certif. PL-300"
    ])
    
    pdf.set_xy(68, 32)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, clean_txt("1. ARCHITECTURE & 3 MOTEURS TECHNIQUE"))
    pdf.set_draw_color(212, 175, 55)
    pdf.line(68, 38, 200, 38)
    pdf.set_xy(68, 40)
    
    p1 = [
        "1. Power Query & M Code : ETL d'extraction, nettoyage et depivotage des tables.",
        "2. Modele en Etoile (Star Schema) : Tables de Faits (ventes/transactions) vs Tables de Dimensions (dates, clients, produits).",
        "3. Langage DAX : Mesures dynamiques via CALCULATE, SAMEPERIODLASTYEAR, TOTALYTD et DIVIDE."
    ]
    
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    for p in p1:
        pdf.set_x(68)
        pdf.multi_cell(132, 3.6, clean_txt(p))
        pdf.ln(1.5)
        
    pdf.ln(3)
    pdf.set_x(68)
    pdf.set_font('Times', 'B', 10.5)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(132, 5, clean_txt("2. CAS D'USAGE METIER (MANAGEMENT & CHR/VENTE)"))
    pdf.line(68, pdf.get_y() + 5, 200, pdf.get_y() + 5)
    pdf.set_xy(68, pdf.get_y() + 7)
    
    p2 = [
        "Dashboard P&L Financier : Suivi du CA, Marge EBITDA %, Prime Cost % et waterfall des charges.",
        "Dashboard Performance Ventes : Entonnoir de conversion CRM, panier moyen et KPIs vendeurs.",
        "Dashboard Hotel Hybride & F&B : RevPAR, ADR, captage resto/rooftop et part de reservation directe vs OTAs."
    ]
    
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(226, 232, 240)
    for p in p2:
        pdf.set_x(68)
        pdf.multi_cell(132, 3.6, clean_txt(p))
        pdf.ln(1.5)

    pdf.output(out_path)
    print(f"✅ PDF généré : {out_path}")

if __name__ == "__main__":
    out_dir = "Projets/prospection job/jost-hotel-bordeaux/04_Livrables/PDF"
    bi_dir = "Projets/Outils-BI/Power-BI/04_Livrables/PDF"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(bi_dir, exist_ok=True)
    
    build_cover_letter_pdf(os.path.join(out_dir, "2026-07-29_Matrice_Correlation_Et_Lettre_Motivation_Julien_JOST.pdf"))
    build_pl_pdf(os.path.join(out_dir, "2026-07-29_PL_Simulation_Et_Formules_Gestion_JOST.pdf"))
    build_questions_pdf(os.path.join(out_dir, "2026-07-29_Guide_5_Questions_Pieges_Financieres_Ruggiero.pdf"))
    build_prices_pdf(os.path.join(out_dir, "2026-07-29_Grille_Tarifaire_Et_Prix_JOST_Bordeaux.pdf"))
    build_strategic_post_pdf(os.path.join(out_dir, "2026-07-31_Analyse_Post_Linkedin_Strategique_MELT_JOST.pdf"))
    build_power_bi_pdf(os.path.join(bi_dir, "2026-07-31_Synthese_Executive_Microsoft_Power_BI.pdf"))


