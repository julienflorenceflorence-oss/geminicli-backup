import requests
import json

def test_post():
    url = "https://script.google.com/macros/s/AKfycbxxkPZBFPRjUAPi_aWtOXsYiMEYnDTvO6y-t0CBKnXKngGDe17OochcXlxUuTwck9UnqQ/exec"
    payload = {
        "action": "check_and_add",
        "dpes": [
            {
                "numero_dpe": "TEST-123456789-A",
                "nom_commune_brut": "Toulouse",
                "adresse_brut": "1 Rue de la Digue",
                "code_postal_brut": "31000",
                "date_etablissement_dpe": "2026-07-01",
                "type_batiment": "Maison",
                "etiquette_dpe": "F",
                "periode_construction": "1948-1974",
                "surface_habitable_logement": 85.5
            }
        ]
    }
    
    print(f"Testing POST request on Web App URL: {url}")
    try:
        response = requests.post(url, json=payload, timeout=20)
        print(f"Response status code: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        body = response.text
        print(f"Response body (first 1000 chars):")
        print(body[:1000])
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_post()
