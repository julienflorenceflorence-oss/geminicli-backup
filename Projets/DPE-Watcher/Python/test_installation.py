import os
import sys
import json
import requests

def run_tests():
    print("=== DPE WATCHER PREMIUM - DIAGNOSTIC ET INSTALLATION ===")
    
    # 1. Verification des bibliotheques
    print("\n[1/3] Verification des dependances Python...")
    libs = {
        "pandas": "pandas (manipulation de donnees)",
        "openpyxl": "openpyxl (moteur Excel)",
        "requests": "requests (requetes HTTP)",
    }
    
    all_ok = True
    for lib, desc in libs.items():
        try:
            __import__(lib)
            print(f"  [OK] {lib} est disponible.")
        except ImportError:
            print(f"  [ERREUR] {lib} ({desc}) est MANQUANT.")
            all_ok = False
            
    if not all_ok:
        print("\n=> Des bibliotheques sont manquantes. Veuillez executer : pip install -r requirements.txt")
    else:
        print("  => Toutes les dependances requises sont installees.")

    # 2. Verification de la configuration
    print("\n[2/3] Verification du fichier config.json...")
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    cfg = None
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
            print("  [OK] Fichier config.json present et syntaxe JSON correcte.")
            cp = cfg.get("filtering", {}).get("codes_postaux", [])
            print(f"  Codes postaux configures : {cp}")
            smtp = cfg.get("email", {}).get("smtp_server", "")
            print(f"  Serveur SMTP configure : {smtp}")
        except Exception as e:
            print(f"  [ERREUR] Le fichier config.json existe mais contient des erreurs : {e}")
    else:
        print("  [ERREUR] Fichier config.json MANQUANT dans le dossier.")

    # 3. Test de connexion a l'API ADEME et Google Sheets
    if cfg:
        print("\n[3/3] Test des connexions Reseau (API ADEME & Google Sheets)...")
        
        # Test ADEME
        dataset_id = "meg-83tjwtg8dyz4vv7h1dqe"
        url_ademe = f"https://data.ademe.fr/data-fair/api/v1/datasets/{dataset_id}/lines?size=1"
        try:
            r = requests.get(url_ademe, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            r.raise_for_status()
            print("  [OK] Connexion et requete API ADEME reussies.")
        except Exception as e:
            print(f"  [ERREUR] Echec de la connexion a l'API ADEME : {e}")
            
        # Test Google Sheets Web App
        web_app_url = cfg.get("google_sheets", {}).get("web_app_url", "")
        if web_app_url and "script.google.com" in web_app_url:
            print(f"  Tentative de ping de la Web App Google Sheets : {web_app_url}")
            try:
                # On simule un appel de test avec un tableau vide
                test_payload = {"action": "check_and_add", "dpes": []}
                r = requests.post(web_app_url, json=test_payload, timeout=20)
                r.raise_for_status()
                res = r.json()
                if "success" in res or "new_dpes" in res:
                    print("  [OK] Connexion et communication avec la Web App Google Sheets reussies.")
                else:
                    print(f"  [AVERTISSEMENT] Reponse Google Sheets inattendue : {res}")
            except Exception as e:
                print(f"  [ERREUR] Echec de communication avec la Web App Google Sheets : {e}")
                print("  Veuillez verifier que vous avez deploye le script en 'Application Web' accessible par 'Anyone' et que l'URL est correcte.")
        else:
            print("  [INFO] URL Google Sheets non configuree dans config.json (ou valeur par defaut). Test ignore.")

    print("\n=== DIAGNOSTIC TERMINE ===")

if __name__ == "__main__":
    run_tests()
