import os
import sys
import json
import csv
import re
from datetime import datetime
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/documents'
]

CRED_PATH = "/Users/admin/Desktop/geminicli-backup/Projets/Memoire-Bachelor/03_Travail/agent soutenance/Data/2026-07-25_credentials.json"
TOKEN_PATH = "/Users/admin/Desktop/geminicli-backup/Projets/Memoire-Bachelor/03_Travail/agent soutenance/Data/2026-07-25_token.json"

OUTPUT_CSV = "/Users/admin/Desktop/geminicli-backup/04_Livrables/Data/2026-09-20_QUESTIA_Extraction_Gmail_Data.csv"
OUTPUT_JSON = "/Users/admin/Desktop/geminicli-backup/04_Livrables/Data/2026-09-20_QUESTIA_Extraction_Gmail_Data.json"

def get_gmail_service():
    if not os.path.exists(TOKEN_PATH):
        raise FileNotFoundError(f"Token file not found at {TOKEN_PATH}")
    
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, 'w') as f:
            f.write(creds.to_json())
            
    service = build('gmail', 'v1', credentials=creds)
    return service

def extract_email_data(search_query="", max_results=20):
    service = get_gmail_service()
    print(f"🔍 Searching Gmail for query: '{search_query}' (max {max_results} messages)...")
    
    results = service.users().messages().list(userId='me', q=search_query, maxResults=max_results).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print("No messages found matching query.")
        return []
    
    extracted_records = []
    
    for idx, msg in enumerate(messages):
        msg_id = msg['id']
        m_data = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        
        headers = m_data.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '(Sans objet)')
        sender = next((h['value'] for h in headers if h['name'].lower() == 'from'), '(Expéditeur inconnu)')
        date_str = next((h['value'] for h in headers if h['name'].lower() == 'date'), '')
        snippet = m_data.get('snippet', '')
        
        # Extract Sender Name & Email
        email_match = re.search(r'<([^>]+)>', sender)
        sender_email = email_match.group(1) if email_match else sender
        sender_name = re.sub(r'<[^>]+>', '', sender).strip()
        
        record = {
            'id': msg_id,
            'date': date_str,
            'sender_name': sender_name,
            'sender_email': sender_email,
            'subject': subject,
            'snippet': snippet,
            'extracted_at': datetime.now().isoformat()
        }
        extracted_records.append(record)
        print(f"[{idx+1}/{len(messages)}] Extracted: {subject} | From: {sender_name} ({sender_email})")

    # Save to CSV
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    with open(OUTPUT_CSV, mode='w', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'date', 'sender_name', 'sender_email', 'subject', 'snippet', 'extracted_at']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extracted_records)

    # Save to JSON
    with open(OUTPUT_JSON, mode='w', encoding='utf-8') as f:
        json.dump(extracted_records, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Extraction complete! Extracted {len(extracted_records)} emails.")
    print(f"📄 Saved CSV to: {OUTPUT_CSV}")
    print(f"📄 Saved JSON to: {OUTPUT_JSON}")
    
    return extracted_records

if __name__ == '__main__':
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    extract_email_data(query, limit)
