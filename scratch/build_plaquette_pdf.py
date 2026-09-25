import sys
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Top gold banner
        self.setFillColor(colors.HexColor('#D4AF37'))
        self.rect(0, A4[1] - 8, A4[0], 8, stroke=0, fill=1)
        
        # Footer
        self.setFont("Helvetica-Bold", 8.5)
        self.setFillColor(colors.HexColor('#64748B'))
        self.drawString(40, 22, "Moteur de Détection d'Entreprises en Recherche Active • Julien FLORENCE (06 61 74 75 73)")
        page_text = f"Page {self._pageNumber} / {page_count}"
        self.drawRightString(A4[0] - 40, 22, page_text)
        
        self.setStrokeColor(colors.HexColor('#CBD5E1'))
        self.setLineWidth(0.8)
        self.line(40, 34, A4[0] - 40, 34)
        self.restoreState()

def generate_pdf():
    pdf_root = "/Users/admin/Desktop/geminicli-backup/Plaquette_Commerciale_Detection_Entreprises.pdf"
    pdf_livrable = "/Users/admin/Desktop/geminicli-backup/04_Livrables/PDF/Plaquette_Commerciale_Detection_Entreprises.pdf"
    
    os.makedirs(os.path.dirname(pdf_livrable), exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_root,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()
    
    GOLD = colors.HexColor('#D4AF37')
    CYAN = colors.HexColor('#0284C7')
    TEXT_MAIN = colors.HexColor('#0F172A')
    TEXT_SUB = colors.HexColor('#475569')
    CARD_BG = colors.HexColor('#F8FAFC')
    BORDER_COLOR = colors.HexColor('#CBD5E1')

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=GOLD
    )

    sub_title_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=CYAN
    )

    h2_style = ParagraphStyle(
        'SecHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=GOLD,
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=TEXT_MAIN
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_MAIN
    )

    price_header = ParagraphStyle('PriceH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=GOLD, alignment=1)
    price_val = ParagraphStyle('PriceV', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=16, leading=19, textColor=colors.HexColor('#000000'), alignment=1)
    price_feat = ParagraphStyle('PriceF', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=TEXT_MAIN)

    story = []

    # --- HEADER ---
    header_data = [
        [
            Paragraph("<b>MOTEUR DE DÉTECTION D'ENTREPRISES EN RECHERCHE ACTIVE</b><br/><font size=10 color='#0284C7'>Salariés • Alternants • POE • Stagiaires</font>", title_style),
            Paragraph("<b>PLAQUETTE COMMERCIALE OFFICIELLE</b><br/>Julien FLORENCE<br/>Direction Commerciale B2B<br/>📞 06 61 74 75 73", ParagraphStyle('HMeta', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, alignment=2, textColor=TEXT_SUB))
        ]
    ]
    t_header = Table(header_data, colWidths=[330, 190])
    t_header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=10))

    # --- INTRO CALLOUT ---
    callout_data = [
        [Paragraph("<b>Ne prospectez plus sur des fichiers morts :</b> Nous ne vendons pas des annuaires d'entreprises passives. Notre moteur détecte en temps réel les entreprises qui <b>publient des offres d'emploi actives en ce moment</b> (2+ postes ouverts), rattachées à leur branche/OPCO et enrichies du nom et téléphone direct/portable du dirigeant ou DRH.", callout_style)]
    ]
    t_callout = Table(callout_data, colWidths=[520])
    t_callout.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEFCE8')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FDE047')),
        ('LINELEFT', (0,0), (-1,-1), 4, GOLD),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_callout)
    story.append(Spacer(1, 10))

    # --- SECTION 1 : COMPARATIF ---
    story.append(Paragraph("1. La Rupture : Fichier Statique vs Détection d'Intention en Temps Réel", h2_style))
    
    grid1_data = [
        [
            Paragraph("<b>Fichiers Classiques du Commerce</b><br/>• Fichiers statiques SIRENE / NAF.<br/>• 95% d'entreprises ne recrutant pas aujourd'hui.<br/>• Numéro de standard généraliste (barrage d'accueil).<br/>• Aucune donnée sur la branche ou l'OPCO.", body_style),
            Paragraph("<b>Notre Moteur de Détection Temps Réel</b><br/>• Détection des offres d'emploi ouvertes (2+ postes).<br/>• 5 lignes seulement sur 100 retenues après filtre.<br/>• 77% avec téléphone direct / portable du décideur.<br/>• Branche professionnelle & OPCO reconstitués.", body_style)
        ]
    ]
    t_grid1 = Table(grid1_data, colWidths=[250, 255])
    t_grid1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_grid1)
    story.append(Spacer(1, 10))

    # --- SECTION 2 : A QUI S'ADRESSE CE SERVICE ---
    story.append(Paragraph("2. Pour Qui ? (Organismes, CFAs, Agences & Écoles)", h2_style))
    
    cibles_data = [
        [
            Paragraph("<b>CFAs & Alternance</b><br/>Placer vos étudiants et débloquer les financements OPCO (6k€-10k€) avant la date limite.", body_style),
            Paragraph("<b>Organismes POE / POEC</b><br/>Obtenir les engagements d'embauche indispensables à l'ouverture des promos.", body_style)
        ],
        [
            Paragraph("<b>Intérim & Recrutement (ETT)</b><br/>Donner chaque matin aux commerciaux la liste des entreprises qui cherchent des salariés.", body_style),
            Paragraph("<b>Écoles Supérieures</b><br/>Alimenter le service carrières en opportunités de stages et 1er emploi.", body_style)
        ]
    ]
    t_cibles = Table(cibles_data, colWidths=[250, 255])
    t_cibles.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_cibles)

    # --- PAGE 2 BREAK ---
    story.append(PageBreak())

    # --- PAGE 2 HEADER ---
    story.append(t_header)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=10))

    # --- SECTION 3 : PRICING CARDS ---
    story.append(Paragraph("3. Formules & Grille Tarifaire Officielle", h2_style))

    pricing_data = [
        [
            Paragraph("PACK STARTER", price_header),
            Paragraph("PACK RÉGIONAL ⭐", price_header),
            Paragraph("PACK NATIONAL", price_header)
        ],
        [
            Paragraph("1 500 € HT", price_val),
            Paragraph("2 500 € HT", price_val),
            Paragraph("7 500 € HT", price_val)
        ],
        [
            Paragraph("• 1 Département / 1 Filière ciblée<br/>• 300 à 500 Entreprises détectées<br/>• Coordonnées Dirigeant/RH directes<br/>• Fichier CSV/Excel prêt à prospecter", price_feat),
            Paragraph("• 1 Région entière (ex: Occitanie / IDF)<br/>• Pipeline continu pendant 6 mois<br/>• 3 000 à 5 000 Entreprises qualifiées<br/>• Branche & OPCO reconstitués<br/>• Suivi & accompagnement dédié", price_feat),
            Paragraph("• France Entière / Toutes branches<br/>• 50 000+ à 100 000 Leads livrés<br/>• Flux automatisé dans votre CRM<br/>• Accompagnement 6-12 mois dédié", price_feat)
        ]
    ]
    t_pricing = Table(pricing_data, colWidths=[165, 175, 165])
    t_pricing.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#FEF08A')),
        ('BACKGROUND', (1,0), (1,-1), colors.HexColor('#FEFCE8')),
        ('BOX', (0,0), (-1,-1), 1, GOLD),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_pricing)
    story.append(Spacer(1, 14))

    # --- SECTION 4 : ROI CALCULATOR ---
    story.append(Paragraph("4. Calculateur de Rentabilité Immédiate (Le ROI No-Brainer)", h2_style))

    roi_data = [
        [Paragraph("<b>Un seul alternant non placé</b> représente une perte de <b>6 000 € à 9 000 €</b> de budget OPCO pour votre centre. Une promo POEC annulée représente <b>30 000 € de CA perdu</b>.<br/>En souscrivant au Pack Régional à 2 500 € HT, <b>2 seuls placements réussis rentabilisent l'intégralité de votre investissement. Tout le reste est de la marge pure.</b>", callout_style)]
    ]
    t_roi = Table(roi_data, colWidths=[520])
    t_roi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, CYAN),
        ('LINELEFT', (0,0), (-1,-1), 4, CYAN),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_roi)
    story.append(Spacer(1, 14))

    # --- CONTACT BLOCK ---
    story.append(Paragraph("5. Prise de Contact & Réservation", h2_style))
    story.append(Paragraph("<b>Julien FLORENCE — Direction Commerciale & Stratégie B2B</b><br/>📞 Direct : 06 61 74 75 73 | 📧 Email : julienflorence.florence@gmail.com<br/>🌐 Hub Exécutif : <i>https://julienflorenceflorence-oss.github.io/geminicli-backup/</i>", body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    
    import shutil
    shutil.copyfile(pdf_root, pdf_livrable)
    print(f"Plaquette PDF compiled at {pdf_root} and {pdf_livrable}")

if __name__ == "__main__":
    generate_pdf()
