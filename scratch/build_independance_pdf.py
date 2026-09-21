import sys
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

def generate_memo_pdf(output_paths):
    for output_path in output_paths:
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=1.5*cm,
            leftMargin=1.5*cm,
            topMargin=1.2*cm,
            bottomMargin=1.2*cm
        )

        styles = getSampleStyleSheet()

        # COLOR PALETTE (CYBER GOLD EXECUTIVE THEME)
        DARK_BLUE = colors.HexColor("#0B0E14")
        NAVY_SURFACE = colors.HexColor("#131822")
        GOLD_MAIN = colors.HexColor("#B89628")
        GOLD_LIGHT = colors.HexColor("#D4AF37")
        CYAN_ACCENT = colors.HexColor("#0284C7")
        TEXT_DARK = colors.HexColor("#1E293B")
        TEXT_MUTED = colors.HexColor("#64748B")
        BG_LIGHT = colors.HexColor("#F8FAFC")
        BORDER_GOLD = colors.HexColor("#CBD5E1")

        # TYPOGRAPHY STYLES
        style_doc_title = ParagraphStyle(
            'DocTitle',
            fontName='Helvetica-Bold',
            fontSize=18,
            leading=22,
            textColor=DARK_BLUE
        )

        style_doc_subtitle = ParagraphStyle(
            'DocSubtitle',
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=14,
            textColor=CYAN_ACCENT
        )

        style_h2 = ParagraphStyle(
            'SectionH2',
            fontName='Helvetica-Bold',
            fontSize=12,
            leading=16,
            textColor=GOLD_MAIN,
            spaceBefore=10,
            spaceAfter=4
        )

        style_body = ParagraphStyle(
            'Body',
            fontName='Helvetica',
            fontSize=9.5,
            leading=13.5,
            textColor=TEXT_DARK
        )

        style_body_bold = ParagraphStyle(
            'BodyBold',
            fontName='Helvetica-Bold',
            fontSize=9.5,
            leading=13.5,
            textColor=TEXT_DARK
        )

        style_pitch_box = ParagraphStyle(
            'PitchBox',
            fontName='Helvetica-Oblique',
            fontSize=9,
            leading=13,
            textColor=DARK_BLUE
        )

        story = []

        # --- HEADER TABLE WITH PROFILE & EVENT INFO ---
        qr_code_path = "/Users/admin/Desktop/geminicli-backup/QR_Code_Carte_De_Visite.png"
        photo_path = "/Users/admin/Desktop/geminicli-backup/julien_florence_photo.jpg"

        header_cell_left = [
            Paragraph("INDÉPENDANCE DAY #3 — MÉMO STRATÉGIQUE", style_doc_title),
            Spacer(1, 4),
            Paragraph("ACCÉLÉRATEUR BUSINESS & NETWORKING PREMIUM • MARDI 22 SEPTEMBRE 2026", style_doc_subtitle),
            Spacer(1, 4),
            Paragraph("<b>Julien FLORENCE</b> — Direction Commerciale • BU Manager • Management de Transition<br/><i>Co-Fondateur QuestIA • Pass Premium VIP</i>", style_body)
        ]

        qr_img = Image(qr_code_path, width=2.2*cm, height=2.2*cm) if os.path.exists(qr_code_path) else Paragraph("QR", style_body)

        header_table = Table([[header_cell_left, qr_img]], colWidths=[14.5*cm, 3.5*cm])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
            ('BOX', (0,0), (-1,-1), 1, BORDER_GOLD),
            ('PADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(header_table)
        story.append(Spacer(1, 10))

        story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD_MAIN, spaceAfter=8))

        # --- SECTION 1: FICHE ÉVÉNEMENT & CONTEXTE ---
        story.append(Paragraph("1. FICHE SYNTHÈSE DE L'ÉVÉNEMENT", style_h2))

        event_data = [
            [Paragraph("<b>Événement</b>", style_body_bold), Paragraph("INDÉPENDANCE DAY #3 (Organisé par Eagle Eye Digital / Nassim Amisse)", style_body)],
            [Paragraph("<b>Date & Lieu</b>", style_body_bold), Paragraph("Mardi 22 Septembre 2026 • Centre de Congrès DIAGORA (Labège / Toulouse)", style_body)],
            [Paragraph("<b>Public Cible</b>", style_body_bold), Paragraph("+300 Solopreneurs, Freelances, Consultants B2B, Coachs d'affaires, Dirigeants de TPE", style_body)],
            [Paragraph("<b>Votre Statut</b>", style_body_bold), Paragraph("<b>Pass Premium VIP</b> (Accès complet Conférences, Ateliers, Déjeuner VIP & Replay)", style_body)]
        ]
        t_event = Table(event_data, colWidths=[4*cm, 14*cm])
        t_event.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,-1), BG_LIGHT),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_GOLD),
            ('PADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        story.append(t_event)
        story.append(Spacer(1, 10))

        # --- SECTION 2: CARTOGRAPHIE INTERVENANTS & SPONSORS ---
        story.append(Paragraph("2. CARTOGRAPHIE DES INTERVENANTS & SPONSORS CLÉS", style_h2))

        speakers_data = [
            [Paragraph("<b>Intervenant / Partenaire</b>", style_body_bold), Paragraph("<b>Expertise & Rôle</b>", style_body_bold), Paragraph("<b>Angle de Synergie pour Julien</b>", style_body_bold)],
            [Paragraph("<b>Nassim Amisse</b><br/>Eagle Eye Digital", style_body), Paragraph("Organisateur, Acquisition B2B High-Ticket & LinkedIn", style_body), Paragraph("Direction Commerciale partagée pour ses clients agences/TPE", style_body)],
            [Paragraph("<b>Kanbox</b><br/>(Sponsor Principal)", style_body), Paragraph("CRM & Outbound Email/Phone directement sur LinkedIn", style_body), Paragraph("Intégration d'IA & scripts psychométriques (QuestIA Sales Engine)", style_body)],
            [Paragraph("<b>Jean Carrière</b>", style_body), Paragraph("Prospection LinkedIn automatisée & Scraping", style_body), Paragraph("Couplage avec détection de signaux d'embauche & branches OPCO", style_body)],
            [Paragraph("<b>Jimmy Beteau</b>", style_body), Paragraph("Coaching d'affaires & passage à l'échelle TPE/PME", style_body), Paragraph("Recommandation réciproque sur l'ingénierie commerciale P&L", style_body)],
            [Paragraph("<b>Maya Caballero</b>", style_body), Paragraph("Closing éthique & Vente pour profils techniques", style_body), Paragraph("Structuration du pipeline commercial B2B post-closing", style_body)]
        ]
        t_speakers = Table(speakers_data, colWidths=[4.5*cm, 6.5*cm, 7*cm])
        t_speakers.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_GOLD),
            ('PADDING', (0,0), (-1,-1), 5),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(t_speakers)
        story.append(Spacer(1, 10))

        # --- SECTION 3: MATRICE DES OPPORTUNITÉS STRATÉGIQUES ---
        story.append(Paragraph("3. LES 4 AXES D'OPPORTUNITÉS POUR JULIEN FLORENCE", style_h2))

        opp_data = [
            [Paragraph("<b>Axe 1 : Direction Commerciale Partagée (Fractional CRO)</b>", style_body_bold)],
            [Paragraph("Accompagner les agences et dirigeants de TPE qui plafonnent (50k€-150k€) en structurant leur force de vente, leur P&L et leur closing B2B sans le coût d'un cadre plein temps.", style_body)],
            [Paragraph("<b>Axe 2 : Synergies Tech Outbound & QuestIA Sales Engine</b>", style_body_bold)],
            [Paragraph("S'associer aux acteurs de l'automation (Kanbox, Jean Carrière) pour apporter la brique d'IA qualifiante (détection des recrutements actifs + ciblage psychométrique DISC/PCM).", style_body)],
            [Paragraph("<b>Axe 3 : Prospection & Décrochage de Financements POE/POEC</b>", style_body_bold)],
            [Paragraph("Vendre aux organismes de formation et membres du BNI des fichiers d'entreprises qui recrutent réellement avec ligne directe des dirigeants pour débloquer les financements OPCO.", style_body)],
            [Paragraph("<b>Axe 4 : Démonstration Personal Branding Cyber Gold</b>", style_body_bold)],
            [Paragraph("Utiliser le Pass Premium lors du déjeuner VIP et faire scanner le QR Code interactif vers le Hub Exécutif 3D (VCard instantané + Portfolio Diplômes).", style_body)]
        ]
        t_opp = Table(opp_data, colWidths=[18*cm])
        t_opp.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), BG_LIGHT),
            ('BACKGROUND', (0,2), (-1,2), BG_LIGHT),
            ('BACKGROUND', (0,4), (-1,4), BG_LIGHT),
            ('BACKGROUND', (0,6), (-1,6), BG_LIGHT),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_GOLD),
            ('PADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(t_opp)
        story.append(Spacer(1, 10))

        # --- SECTION 4: PITCHS TERRAIN & BATTLECARDS ---
        story.append(Paragraph("4. ACCROCHES & PITCHS TERRAIN (BATTLECARDS NETWORKING)", style_h2))

        pitch_1 = Paragraph("<b>Pitch 1 — Face à un Dirigeant de TPE / Agence B2B :</b><br/><i>« J'interviens comme Directeur Commercial en temps partagé pour les structures qui veulent passer un cap. J'associe 20 ans de pilotage P&L (+140% CA) à des algorithmes d'IA de détection de signaux d'achat. Et vous, comment est structurée votre force de vente actuellement ? »</i>", style_pitch_box)
        pitch_2 = Paragraph("<b>Pitch 2 — Face à Kanbox / Jean Carrière (Tech Outreach) :</b><br/><i>« De mon côté avec QuestIA, nous couplons le scraping d'offres d'emploi à la qualification psychologique DISC/PCM des décideurs pour multiplier les taux de conversion B2B par 3. On devrait échanger sur une synergie de co-selling ! »</i>", style_pitch_box)
        pitch_3 = Paragraph("<b>Pitch 3 — Face à un Organisme de Formation / Consultant BNI :</b><br/><i>« Le plus dur sur les POEC, c'est de trouver les entreprises qui s'engagent à embaucher pour déclencher l'OPCO. J'ai développé un pipeline qui livre les lignes directes des dirigeants qui recrutent sur vos métiers en 24h. »</i>", style_pitch_box)

        t_pitch = Table([[pitch_1], [Spacer(1,3)], [pitch_2], [Spacer(1,3)], [pitch_3]], colWidths=[18*cm])
        t_pitch.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), BG_LIGHT),
            ('BACKGROUND', (0,2), (0,2), BG_LIGHT),
            ('BACKGROUND', (0,4), (0,4), BG_LIGHT),
            ('BOX', (0,0), (0,0), 1, GOLD_MAIN),
            ('BOX', (0,2), (0,2), 1, CYAN_ACCENT),
            ('BOX', (0,4), (0,4), 1, GOLD_MAIN),
            ('PADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(t_pitch)
        story.append(Spacer(1, 10))

        # --- SECTION 5: FOOTER HUB DIGITAL ---
        story.append(HRFlowable(width="100%", thickness=1, color=GOLD_MAIN, spaceAfter=6))
        footer_text = Paragraph("<b>HUB EXÉCUTIF DIGITAL & CONTACT DIRECT :</b><br/>"
                                "🌐 site web : <u>https://julienflorenceflorence-oss.github.io/geminicli-backup/</u><br/>"
                                "📱 Téléphone : 06 61 74 75 73 • 📧 Email : julienflorence.florence@gmail.com • Toulouse Métropole", style_doc_subtitle)
        story.append(footer_text)

        doc.build(story)
        print(f"Generated PDF successfully: {output_path}")

if __name__ == "__main__":
    targets = [
        "/Users/admin/Desktop/geminicli-backup/Memo_Strategique_Independance_Day_3.pdf",
        "/Users/admin/Desktop/geminicli-backup/04_Livrables/PDF/Memo_Strategique_Independance_Day_3.pdf"
    ]
    generate_memo_pdf(targets)
