import os
import subprocess
import re
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

# CONFIGURATION
PHONE_IP = "192.168.1.50"  # Remplacer par l'adresse IP de votre téléphone Android en Wi-Fi
PHONE_PORT = "5555"
ANDROID_DIR = "/sdcard/CubeCallRecorder"  # Répertoire par défaut de Cube ACR sur Android
LOCAL_DIR = r"C:\Users\julien\OneDrive\Bureau\geminicli\Projets\Memoire-Bachelor\02_Sources\CubeACR_Sync"

os.makedirs(LOCAL_DIR, exist_ok=True)

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return "", str(e)

def check_adb():
    # Vérifie si adb est accessible
    out, err = run_cmd("adb --version")
    if not out:
        print("Error: ADB is not installed or not added to PATH on your PC.")
        print("Please download platform-tools (ADB) for Windows and add it to your PATH.")
        return False
    return True

def connect_phone():
    print(f"Connecting to Android phone at {PHONE_IP}:{PHONE_PORT}...")
    run_cmd(f"adb disconnect")
    out, err = run_cmd(f"adb connect {PHONE_IP}:{PHONE_PORT}")
    print(out)
    if "connected to" in out:
        return True
    return False

def sync_recordings():
    print("Listing files on Android phone...")
    # Lister les fichiers dans le dossier Cube ACR du téléphone
    out, err = run_cmd(f"adb shell ls {ANDROID_DIR}")
    if err:
        print(f"Directory {ANDROID_DIR} not found on phone or permission denied. Error: {err}")
        return
        
    files = out.split()
    print(f"Found {len(files)} files on phone.")
    
    pulled_count = 0
    for f in files:
        # Ne prendre que les fichiers audio
        if not f.lower().endswith(('.mp3', '.wav', '.m4a', '.amr')):
            continue
            
        local_file_path = os.path.join(LOCAL_DIR, f)
        if not os.path.exists(local_file_path):
            print(f"Pulling new recording: {f}...")
            # Commande ADB pull pour copier le fichier du tel au PC
            out_p, err_p = run_cmd(f'adb pull "{ANDROID_DIR}/{f}" "{local_file_path}"')
            if not err_p:
                pulled_count += 1
            else:
                print(f"Failed to pull {f}: {err_p}")
                
    print(f"Sync complete. Pulled {pulled_count} new recording(s) to PC.")
    sys.stdout.flush()

if __name__ == "__main__":
    if check_adb():
        if connect_phone():
            sync_recordings()
        else:
            print("Failed to connect to phone over Wi-Fi.")
            print("Make sure your phone is on the same Wi-Fi, Developer Options are enabled, and 'adb tcpip 5555' was run once via USB.")
    sys.stdout.flush()
