import json
import requests
import os

def test_post_from_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Projets", "DPE-Watcher", "Python", "config.json")
    print(f"Reading config from: {config_path}")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        url = cfg.get("google_sheets", {}).get("web_app_url", "")
        print(f"Testing POST request on Web App URL: {url}")
        
        payload = {
            "action": "check_and_add",
            "dpes": [
                {
                    "numero_dpe": "TEST-POST-VALIDE-99",
                    "nom_commune_brut": "Carcassonne",
                    "adresse_brut": "10 Rue de la Paix",
                    "code_postal_brut": "11000",
                    "date_etablissement_dpe": "2026-07-04",
                    "type_batiment": "Maison",
                    "etiquette_dpe": "G",
                    "periode_construction": "Avant 1948",
                    "surface_habitable_logement": 120.0
                }
            ]
        }
        
        response = requests.post(url, json=payload, timeout=20)
        print(f"Response status code: {response.status_code}")
        body = response.text
        print(f"Response body (first 1000 chars):")
        print(body[:1000])
        
        try:
            data = response.json()
            print("SUCCESS! Successfully parsed JSON from POST Web App.")
            print(f"Response data: {data}")
        except json.JSONDecodeError:
            print("FAILED to parse JSON. Response is not valid JSON.")
            
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_post_from_config()
