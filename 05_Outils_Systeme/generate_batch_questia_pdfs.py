#!/usr/bin/env python3
"""
Script de Génération en Lot (Batch) des PDFs QuestIA LAB à partir d'un fichier CSV.
Lit chaque ligne d'un fichier CSV de prospects et génère un PDF personnalisé
intégalement rédigé avec la charte QuestIA LAB et le logo PNG.
"""

import sys
import os
import csv
import argparse

# Dynamic import of single custom PDF generator
sys.path.insert(0, '/Users/admin/Desktop/geminicli-backup/05_Outils_Systeme')
from generate_custom_questia_pdf import generate_custom_pdf

def generate_batch_from_csv(csv_path, out_dir):
    if not os.path.exists(csv_path):
        print(f"❌ Erreur : Fichier CSV non trouvé -> {csv_path}")
        return

    os.makedirs(out_dir, exist_ok=True)
    
    generated_files = []
    
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        # Detect delimiter (; or ,)
        sample = f.read(2048)
        f.seek(0)
        delimiter = ';' if ';' in sample else ','
        
        reader = csv.DictReader(f, delimiter=delimiter)
        
        print(f"🚀 Début de la génération en lot depuis {csv_path}...")
        print("=" * 70)
        
        for idx, row in enumerate(reader, 1):
            company = row.get("Entreprise") or row.get("company") or f"Entreprise_{idx}"
            prospect = row.get("Contact_Nom") or row.get("contact") or "Monsieur le Directeur"
            title = row.get("Titre_Fonction") or row.get("title") or "VP Sales / DG"
            sector = row.get("Secteur_ICP") or row.get("icp") or "Aéronautique"
            
            try:
                revenue_raw = str(row.get("CA_Export_EUR") or row.get("revenue") or "10000000")
                revenue_num = float(revenue_raw.replace(" ", "").replace("EUR", "").replace("€", ""))
                revenue_str = f"{int(revenue_num):,} EUR".replace(",", " ")
            except:
                revenue_str = "10 000 000 EUR"
                
            try:
                leak_rate = float(row.get("Taux_Fuite_Marge_PCT") or row.get("leak") or 4.2)
            except:
                leak_rate = 4.2

            # Determine PDF type based on status or index
            status = str(row.get("Statut_Prospect") or "").lower()
            if "refus" in status or "relance" in status:
                pdf_type = "choc_refus"
            elif "réalisé" in status or "visio" in status:
                pdf_type = "confirmatif"
            elif "passe" in status or "barrage" in status or "secretariat" in status:
                pdf_type = "passe_barrage"
            else:
                pdf_type = "choc_refus"

            sanitized_company = "".join([c for c in company if c.isalnum() or c in [' ', '_', '-']]).strip().replace(' ', '_')
            filename = f"QUESTIA LAB_Audit_{idx:02d}_{sanitized_company}.pdf"
            pdf_path = os.path.join(out_dir, filename)

            data = {
                "company": company,
                "prospect": prospect,
                "title_prospect": title,
                "sector": sector,
                "revenue": revenue_str,
                "leak_rate": leak_rate,
                "pdf_type": pdf_type,
                "custom_note": f"Document généré automatiquement en lot pour {company}."
            }

            generate_custom_pdf(data, pdf_path)
            generated_files.append((company, pdf_path))

    print("=" * 70)
    print(f"🎉 Génération terminée ! {len(generated_files)} PDFs générés avec succès sous {out_dir}\n")
    return generated_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur de PDF QuestIA LAB en lot depuis CSV")
    parser.add_argument("--csv", type=str, default="/Users/admin/Desktop/geminicli-backup/04_Livrables/Data/QUESTIA LAB_Exemple_Import_Prospects.csv")
    parser.add_argument("--out", type=str, default="/Users/admin/Desktop/geminicli-backup/04_Livrables/PDF/Batch_Prospects")

    args = parser.parse_args()
    
    generate_batch_from_csv(args.csv, args.out)
