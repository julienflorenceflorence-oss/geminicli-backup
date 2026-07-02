import requests
import json

def test_get():
    url = "https://script.google.com/macros/s/AKfycbz7im0Vrs26tSboh5J9IheAmxdeetWydbRZ9_hlwAXY2GlOh5a8_tGB33J50aKaFfuC/exec"
    print(f"Testing GET request on Web App URL: {url}")
    
    try:
        # requests suit automatiquement les redirections 302
        response = requests.get(url, timeout=20)
        print(f"Response status code: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        body = response.text
        print(f"Response body (first 500 chars): {body[:500]}")
        
        try:
            data = response.json()
            print("Successfully parsed JSON!")
            print(f"JSON keys: {data.keys()}")
            if "dpes" in data:
                print(f"Found {len(data['dpes'])} DPEs in Sheets.")
        except json.JSONDecodeError:
            print("Failed to parse JSON. Response is not valid JSON.")
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_get()
