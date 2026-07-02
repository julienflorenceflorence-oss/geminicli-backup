import urllib.request
import urllib.parse
import json

def list_dpe_datasets():
    url = "https://data.ademe.fr/data-fair/api/v1/datasets"
    params = {
        "size": 100,
        "q": "dpe"
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f"{url}?{query_string}"
    print(f"Requesting catalog: {full_url}")
    
    try:
        req = urllib.request.Request(full_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            print(f"Total datasets found: {data.get('total')}")
            if "results" in data:
                for ds in data["results"]:
                    print(f"ID: {ds.get('id')} | Title: {ds.get('title')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_dpe_datasets()
