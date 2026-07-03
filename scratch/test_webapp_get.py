import json
import requests
import os

def test_get_from_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Projets", "DPE-Watcher", "Python", "config.json")
    print(f"Reading config from: {config_path}")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        url = cfg.get("google_sheets", {}).get("web_app_url", "")
        print(f"Testing GET request on Web App URL from config: {url}")
        
        if not url or "script.google.com" not in url:
            print("Error: Web App URL is invalid or empty in config.")
            return
            
        response = requests.get(url, timeout=20)
        print(f"Response status code: {response.status_code}")
        body = response.text
        print(f"Response body (first 1000 chars): {body[:1000]}")
        
        try:
            data = response.json()
            print("SUCCESS! Successfully parsed JSON from Web App.")
            if "dpes" in data:
                print(f"Found {len(data['dpes'])} DPEs in Sheets.")
        except json.JSONDecodeError:
            print("FAILED to parse JSON. Response is not valid JSON.")
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_get_from_config()
