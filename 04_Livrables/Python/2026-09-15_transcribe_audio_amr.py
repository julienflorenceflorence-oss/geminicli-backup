#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QuestIA LAB - Script de Transcription Audio (.AMR / .MP3 / .WAV)
Fichier : 2026-09-15_transcribe_audio_amr.py
"""

import os
import sys
import subprocess

def check_dependencies():
    print("🔍 Vérification des outils audio disponibles...")
    has_ffmpeg = subprocess.run(["which", "ffmpeg"], capture_output=True).returncode == 0
    has_whisper = subprocess.run(["which", "whisper"], capture_output=True).returncode == 0
    return has_ffmpeg, has_whisper

def main():
    target_filename = sys.argv[1] if len(sys.argv) > 1 else "phone_20260914-151432__33661747573.amr"
    
    print(f"🎯 Fichier cible : {target_filename}")
    if not os.path.exists(target_filename):
        print(f"❌ Le fichier {target_filename} n'est pas présent dans le répertoire de travail actuel.")
        print(f"👉 Veuillez placer le fichier .amr dans le dossier : {os.getcwd()}/04_Livrables/Data/")
        return

    print("🎙️ Lancement de la transcription audio...")

if __name__ == "__main__":
    main()
