import os
import sys
import sqlite3
import urllib.request
import json

def run_tests():
    print("=== DPE WATCHER - TESTS DE DIAGNOSTIC ET D'INSTALLATION ===")
    
    # 1. Verification des bibliotheques
    print("\n[1/4] Verification des dependances Python...")
    libs = {
        "pandas": "pandas (manipulation de donnees)",
        "openpyxl": "openpyxl (moteur Excel)",
        "sqlite3": "sqlite3 (base de donnees interne)",
        "urllib.request": "urllib (requetes HTTP natives)"
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

    # 2. Test de la base de donnees locale SQLite
    print("\n[2/4] Test de la base de donnees local SQLite...")
    test_db = "test_temp.db"
    try:
        conn = sqlite3.connect(test_db)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO test (name) VALUES ('Test Connection')")
        conn.commit()
        cursor.execute("SELECT name FROM test WHERE id = 1")
        row = cursor.fetchone()
        conn.close()
        
        # Nettoyage
        if os.path.exists(test_db):
            os.remove(test_db)
            
        if row and row[0] == 'Test Connection':
            print("  [OK] Creation et ecriture SQLite valides.")
        else:
            print("  [ERREUR] SQLite n'a pas renvoye la bonne valeur.")
    except Exception as e:
        print(f"  [ERREUR] Echec du test SQLite : {e}")

    # 3. Test de connexion a l'API ADEME
    print("\n[3/4] Test de connexion a l'API ADEME (data.ademe.fr)...")
    dataset_id = "meg-83tjwtg8dyz4vv7h1dqe"
    url = f"https://data.ademe.fr/data-fair/api/v1/datasets/{dataset_id}/lines?size=1"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if "results" in data:
                print("  [OK] Connexion et requete API ADEME reussies.")
            else:
                print("  [AVERTISSEMENT] Requete reussie mais format de reponse inattendu.")
    except Exception as e:
        print(f"  [ERREUR] Echec de la connexion a l'API ADEME : {e}")
        print("  Veuillez verifier votre connexion Internet ou si l'API ADEME est momentanement indisponible.")

    # 4. Verification de la configuration
    print("\n[4/4] Verification du fichier config.json...")
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
            print("  [OK] Fichier config.json present et syntaxe JSON correcte.")
            # Verifications simples
            cp = cfg.get("filtering", {}).get("codes_postaux", [])
            print(f"  Codes postaux configures : {cp}")
            smtp = cfg.get("email", {}).get("smtp_server", "")
            print(f"  Serveur SMTP configure : {smtp}")
        except Exception as e:
            print(f"  [ERREUR] Le fichier config.json existe mais contient des erreurs : {e}")
    else:
        print("  [ERREUR] Fichier config.json MANQUANT dans le dossier.")

    print("\n=== DIAGNOSTIC TERMINE ===")

if __name__ == "__main__":
    run_tests()
