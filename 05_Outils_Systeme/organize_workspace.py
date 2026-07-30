#!/usr/bin/env python3
"""
Script d'automatisation de la structuration et de l'archivage de l'espace de travail.
Respecte la règle binaire "Fichier Actif / Archives" et la nomenclature AGENTS.md :

1. Les fichiers actifs principaux (ex: index.html, README.md, AGENTS.md, etc.) conservent leur nom actif à la racine de leur sous-dossier de format.
2. Les fichiers datés / livrables reçoivent le préfixe AAAA-MM-JJ_ d'après leur date de dernière modification (mtime).
3. Organisation par sous-dossiers de format : Python, HTML, PDF, Data, Images, Markdown.
4. Support du mode simulation (--dry-run) et d'application (--apply).
"""

import os
import sys
import re
import argparse
from datetime import datetime
from pathlib import Path

# Dossiers / fichiers système à ignorer
EXCLUDE_DIRS = {
    '.git', '.agents', '.devcontainer', 'scratch', 'node_modules', 
    'venv', '.venv', '__pycache__', '.idea', '.vscode'
}

EXCLUDE_FILES = {
    '.DS_Store', '.gitignore', 'package-lock.json', 'package.json', 'AGENTS.md', 'README.md'
}

# Noms de fichiers actifs spécifiques conservés sans préfixe de date s'ils sont uniques ou configurés
PRESERVE_ACTIVE_FILENAMES = {
    'index.html', 'main.py', 'app.py', 'server.py', 'style.css', 'index.css'
}

# Mappings des extensions de fichiers vers les sous-dossiers de format
FORMAT_MAPPINGS = {
    'Python': ['.py', '.bat', '.sh', '.ps1'],
    'HTML': ['.html', '.htm', '.css'],
    'PDF': ['.pdf'],
    'Data': ['.json', '.csv', '.xml', '.xlsx', '.sqlite', '.db'],
    'Images': ['.png', '.jpg', '.jpeg', '.svg', '.gif'],
    'Markdown': ['.md', '.txt']
}

def get_format_folder(extension: str) -> str:
    ext = extension.lower()
    for folder, extensions in FORMAT_MAPPINGS.items():
        if ext in extensions:
            return folder
    return 'Data'

def get_file_mtime_date(filepath: Path) -> str:
    """Retourne la date de dernière modification au format AAAA-MM-JJ."""
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

def sanitize_and_format_name(filename: str, mtime_date: str) -> str:
    """
    S'assure que le fichier commence par AAAA-MM-JJ_ et nettoie le nom si non préservé.
    """
    if filename.lower() in PRESERVE_ACTIVE_FILENAMES:
        return filename

    date_pattern = r'^\d{4}-\d{2}-\d{2}_'
    stem = Path(filename).stem
    ext = Path(filename).suffix
    
    if re.match(date_pattern, filename):
        new_stem = stem
    else:
        clean_stem = stem.replace(' ', '_').replace('-', '_')
        clean_stem = re.sub(r'_+', '_', clean_stem).strip('_')
        new_stem = f"{mtime_date}_{clean_stem}"
        
    return f"{new_stem}{ext}"

def scan_and_plan(root_dir: Path):
    actions = []
    
    for current_root, dirs, files in os.walk(root_dir):
        # Exclure les répertoires système
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        
        rel_root = Path(current_root).relative_to(root_dir)
        
        # Ignorer le dossier 05_Outils_Systeme lui-même
        if '05_Outils_Systeme' in rel_root.parts:
            continue
            
        for file in files:
            if file in EXCLUDE_FILES or file.startswith('.'):
                continue
                
            file_path = Path(current_root) / file
            
            # Déterminer la date mtime
            mtime_date = get_file_mtime_date(file_path)
            
            # Nouveau nom conforme
            new_filename = sanitize_and_format_name(file, mtime_date)
            
            # Sous-dossier de format
            format_folder = get_format_folder(file_path.suffix)
            
            # Destination idéale
            if rel_root == Path('.') or 'A_classer' in rel_root.parts:
                target_dir = root_dir / '03_Travail' / format_folder
            else:
                if format_folder not in rel_root.parts:
                    target_dir = file_path.parent / format_folder
                else:
                    target_dir = file_path.parent
                    
            target_path = target_dir / new_filename
            
            if file_path != target_path:
                actions.append({
                    'source': file_path,
                    'target': target_path,
                    'filename_change': file != new_filename
                })
                
    return actions

def main():
    parser = argparse.ArgumentParser(description="Script de structuration d'espace de travail selon AGENTS.md")
    parser.add_argument('--dry-run', action='store_true', help="Affiche les actions prévues sans déplacer de fichier")
    parser.add_argument('--apply', action='store_true', help="Exécute les déplacements et renommages réels")
    parser.add_argument('--target', type=str, default='.', help="Répertoire cible")
    
    args = parser.parse_args()
    
    if not args.dry_run and not args.apply:
        print("[!] Spécifiez soit --dry-run soit --apply")
        sys.exit(1)
        
    target_dir = Path(args.target).resolve()
    print(f"[*] Analyse de l'espace de travail : {target_dir}")
    
    actions = scan_and_plan(target_dir)
    
    print(f"[*] Total d'actions identifiées : {len(actions)}\n")
    
    for idx, act in enumerate(actions, 1):
        src_rel = act['source'].relative_to(target_dir)
        tgt_rel = act['target'].relative_to(target_dir)
        
        mode_str = "[DRY-RUN]" if args.dry_run else "[APPLY]"
        print(f"{mode_str} #{idx}")
        print(f"   Source      : {src_rel}")
        print(f"   Destination : {tgt_rel}")
        if act['filename_change']:
            print(f"   Renommage   : Oui ({act['source'].name} -> {act['target'].name})")
        print()
        
        if args.apply:
            act['target'].parent.mkdir(parents=True, exist_ok=True)
            act['source'].rename(act['target'])
            
    if args.dry_run:
        print("[*] Simulation terminée. Aucun fichier n'a été modifié.")
        print("[*] Pour appliquer ces changements, lancez le script avec l'option --apply.")
    elif args.apply:
        print("[✓] Organisation et classement appliqués avec succès !")

if __name__ == '__main__':
    main()
