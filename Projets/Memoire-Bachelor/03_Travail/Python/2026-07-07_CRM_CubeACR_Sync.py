import os
import time
import shutil
import re
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Répertoires de travail
CUBEACR_SYNC_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\Projets\Memoire-Bachelor\02_Sources\CubeACR_Sync"
AUDIO_DEST_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\Projets\Memoire-Bachelor\04_Livrables\Audio"
CSV_PATH = r"C:\Users\julien\OneDrive\Bureau\geminicli\selection_60_gites_prestige.csv"
HTML_TEMPL_PATH = r"C:\Users\julien\.gemini\skills\prestige-document-engine\assets\layout-portfolio.html"
HTML_OUT_PATH = r"C:\Users\julien\OneDrive\Bureau\geminicli\02_Espace_Soutenance\index.html"

# Créer les répertoires s'ils n'existent pas
os.makedirs(AUDIO_DEST_DIR, exist_ok=True)
os.makedirs(CUBEACR_SYNC_DIR, exist_ok=True)

print(f"Monitoring Cube ACR sync directory: {CUBEACR_SYNC_DIR}")
print("Listening for new smartphone sync recordings... (Press Ctrl+C to stop)")
sys.stdout.flush()

processed_files = set(os.listdir(CUBEACR_SYNC_DIR))

def rebuild_crm_html():
    """Reconstruit le fichier index.html avec les lecteurs audio si les fichiers existent."""
    if not os.path.exists(CSV_PATH) or not os.path.exists(HTML_TEMPL_PATH):
        return
        
    df = pd.read_csv(CSV_PATH, dtype=str)
    
    with open(HTML_TEMPL_PATH, "r", encoding="utf-8") as f:
        html_template = f.read()

    cards_html = ""
    for idx, row in df.iterrows():
        name = row.get('nom', '')
        rating = row.get('note', '4.0')
        capacity = row.get('capacity', '20')
        city = row.get('ville', 'Non précisée')
        dept = row.get('departement', '')
        region = row.get('region', '')
        desc = row.get('description', '')
        phone = row.get('tel', 'Non précisé')
        email = row.get('email', 'Non précisé')
        web = row.get('web', '')
        
        # Vérifier s'il y a un enregistrement Cube ACR associé à ce numéro
        clean_phone = re.sub(r'\D', '', str(phone))
        audio_filename = f"enregistrement_{clean_phone}.wav"
        # Prendre en charge aussi le format mp3 natif de Cube ACR
        audio_filename_mp3 = f"enregistrement_{clean_phone}.mp3"
        
        audio_path_wav = os.path.join(AUDIO_DEST_DIR, audio_filename)
        audio_path_mp3 = os.path.join(AUDIO_DEST_DIR, audio_filename_mp3)
        
        active_audio_filename = None
        if os.path.exists(audio_path_wav):
            active_audio_filename = audio_filename
        elif os.path.exists(audio_path_mp3):
            active_audio_filename = audio_filename_mp3
            
        audio_player_html = ""
        if active_audio_filename:
            relative_audio_path = f"../Projets/Memoire-Bachelor/04_Livrables/Audio/{active_audio_filename}"
            audio_player_html = f"""
                <div style="margin-top: 15px; padding: 10px; background: rgba(212, 175, 55, 0.05); border: 1px solid rgba(212, 175, 55, 0.2); border-radius: 5px;">
                    <div style="font-size: 0.75rem; color: var(--accent); margin-bottom: 5px; font-weight: bold; letter-spacing: 1px;">🎤 ENREGISTREMENT MOBILE (CUBE ACR)</div>
                    <audio controls style="width: 100%; height: 28px;">
                        <source src="{relative_audio_path}">
                    </audio>
                </div>
            """

        location_str = city
        if dept or region:
            location_str += f" ({dept}" + (f" - {region}" if region else "") + ")"

        web_btn_html = ""
        if web and str(web).startswith("http"):
            web_btn_html = f'<a href="{web}" class="btn-prestige" target="_blank" style="padding: 6px 12px; font-size: 0.75rem; margin-top: 10px;">Visiter le site</a>'
            
        phone_html = f'<a href="tel:{phone}" style="color: var(--accent); text-decoration: none; transition: 0.3s;" onmouseover="this.style.color=\'var(--accent-glow)\'" onmouseout="this.style.color=\'var(--accent)\'">{phone}</a>' if phone != 'Non précisé' else 'Non précisé'
        email_html = f'<a href="mailto:{email}" style="color: var(--accent); text-decoration: none; transition: 0.3s;" onmouseover="this.style.color=\'var(--accent-glow)\'" onmouseout="this.style.color=\'var(--accent)\'">{email}</a>' if email != 'Non précisé' else 'Non précisé'
        
        cards_html += f"""
            <div class="card" id="gite-{idx}">
                <div class="card-title">{name}</div>
                <div style="color: var(--accent); font-weight: bold; margin-bottom: 10px; font-size: 0.95rem;">
                    ★ {rating} &nbsp;|&nbsp; Capacité : {capacity} personnes
                </div>
                <div style="font-size: 0.85rem; color: var(--text); margin-bottom: 10px; font-style: italic;">
                    {location_str}
                </div>
                <div class="card-content" style="height: 120px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical;">
                    {desc}
                </div>
                <div style="border-top: 1px solid rgba(212, 175, 55, 0.1); padding-top: 15px; margin-top: 15px; font-size: 0.85rem;">
                    <div style="margin-bottom: 6px;"><strong>Tél :</strong> {phone_html}</div>
                    <div style="margin-bottom: 12px;"><strong>Email :</strong> {email_html}</div>
                    {web_btn_html}
                    {audio_player_html}
                </div>
            </div>
        """

    title = "SÉLECTION DES 60 GÎTES D'EXCEPTION"
    subtitle = "Classement 4 et 5 étoiles | Capacité supérieure à 20 personnes"
    footer_left = "© 2026 Happy House - Sélection Prestige"
    footer_right = "Généré par Antigravity Agent"

    html_content = html_template.replace("{{title}}", title)
    html_content = html_content.replace("{{subtitle}}", subtitle)
    html_content = html_content.replace("{{cards}}", cards_html)
    html_content = html_content.replace("{{footer_left}}", footer_left)
    html_content = html_content.replace("{{footer_right}}", footer_right)

    html_content = html_content.replace(
        '<a href="#" class="btn-prestige" style="background: var(--accent); color: var(--bg);">Action Principale</a>',
        '<a href="file:///C:/Users/julien/OneDrive/Bureau/geminicli/selection_60_gites_prestige.csv" class="btn-prestige" style="background: var(--accent); color: var(--bg);">Télécharger le CSV</a>'
    )
    html_content = html_content.replace(
        '<a href="#" class="btn-prestige">Action Secondaire</a>',
        '<a href="https://docs.google.com/spreadsheets/d/1VPek8EHOk36ob-lhrHjMsNUxBmojtT1mTccgkU5ly8Y/edit" class="btn-prestige" target="_blank">Ouvrir le Google Sheet</a>'
    )

    with open(HTML_OUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Reconstructed HTML CRM successfully!")
    sys.stdout.flush()

# Première reconstruction au lancement
rebuild_crm_html()

try:
    while True:
        # Scruter le dossier synchronisé
        current_files = set(os.listdir(CUBEACR_SYNC_DIR))
        new_files = current_files - processed_files
        
        for f in new_files:
            ext = os.path.splitext(f)[1].lower()
            if ext not in [".mp3", ".wav", ".m4a", ".amr"]:
                continue
                
            # Laisser le temps à la synchronisation cloud de se stabiliser
            time.sleep(2.0)
            
            print(f"New Cube ACR recording detected: {f}")
            # Extraction des chiffres du numéro de téléphone depuis le nom du fichier
            # Cube ACR inclut généralement le numéro sous forme de série de chiffres
            numbers = re.findall(r'\d+', f)
            phone_num = None
            for num in numbers:
                if len(num) >= 9:  # Un numéro de téléphone fait au moins 9 chiffres
                    phone_num = num
                    break
                    
            if phone_num:
                clean_target_phone = re.sub(r'\D', '', phone_num)
                # Si le numéro commence par un indicatif pays (ex: 336...), on prend les 9 derniers chiffres
                if len(clean_target_phone) > 10 and clean_target_phone.startswith('33'):
                    clean_target_phone = '0' + clean_target_phone[2:]
                    
                print(f"Extracted phone number from filename: {clean_target_phone}")
                
                # Chercher dans la base CSV le gîte correspondant
                if os.path.exists(CSV_PATH):
                    df = pd.read_csv(CSV_PATH, dtype=str)
                    matched_row = None
                    for idx, row in df.iterrows():
                        row_phone = re.sub(r'\D', '', str(row.get('tel', '')))
                        if len(row_phone) > 10 and row_phone.startswith('33'):
                            row_phone = '0' + row_phone[2:]
                            
                        if row_phone and (clean_target_phone in row_phone or row_phone in clean_target_phone):
                            matched_row = row
                            break
                            
                    if matched_row is not None:
                        gite_name = matched_row.get('nom')
                        print(f"Matched with gîte: {gite_name}")
                        
                        # Copier le fichier dans les livrables
                        dest_filename = f"enregistrement_{clean_target_phone}{ext}"
                        dest_path = os.path.join(AUDIO_DEST_DIR, dest_filename)
                        shutil.copy(os.path.join(CUBEACR_SYNC_DIR, f), dest_path)
                        print(f"Audio file copied to: {dest_path}")
                        
                        # Mettre à jour l'HTML du CRM
                        rebuild_crm_html()
                    else:
                        print(f"No matching gîte found for phone: {clean_target_phone}")
                else:
                    print("CSV database not found.")
            else:
                print(f"Could not extract a valid phone number from filename: {f}")
            
            processed_files.add(f)
            
        time.sleep(5)
except KeyboardInterrupt:
    print("\nStopping Cube ACR monitoring daemon.")
