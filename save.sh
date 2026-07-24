#!/bin/bash
# Script de sauvegarde ultra-rapide 1-clic pour Mac / Linux / GitHub Codespaces

MSG="${1:-Sauvegarde automatique - $(date '+%Y-%m-%d %H:%M')}"

echo "🔄 Sauvegarde en cours sur GitHub..."
git add .
git commit -m "$MSG"
git push origin main
echo "✅ Synchronisation GitHub terminée !"
