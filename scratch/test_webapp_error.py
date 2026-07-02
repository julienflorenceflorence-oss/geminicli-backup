import requests

def print_full_error():
    url = "https://script.google.com/macros/s/AKfycbz7im0Vrs26tSboh5J9IheAmxdeetWydbRZ9_hlwAXY2GlOh5a8_tGB33J50aKaFfuC/exec"
    try:
        response = requests.get(url, timeout=20)
        print("Status code:", response.status_code)
        body = response.text
        # Trouver le message d'erreur s'il y en a un
        print("Response body:")
        print(body)
    except Exception as e:
        print("Request failed:", e)

if __name__ == "__main__":
    print_full_error()
