# 📱 Guide de Synchronisation Android ➔ PC pour Enregistrements d'Appels

Ce guide documente la mise en place d'un système de synchronisation sans fil (Wi-Fi local) entre votre smartphone Android (équipé de **Cube ACR**) et votre PC Windows, en utilisant **ADB (Android Debug Bridge)**.

---

## 🛠️ Prérequis sur le Smartphone Android
Pour autoriser votre PC à lire les fichiers du téléphone via Wi-Fi :

1. **Activer les Options pour les Développeurs** :
   * Allez dans *Paramètres* ➔ *À propos du téléphone* ➔ Appuyez **7 fois** sur *Numéro de build*.
2. **Activer le Débogage USB** :
   * Allez dans *Paramètres* ➔ *Système* ➔ *Options pour les développeurs* ➔ Activez **Débogage USB**.

---

## ⚙️ Première Connexion (Initialisation sur le PC)
Vous devez connecter votre téléphone en USB au PC **une seule fois** pour autoriser la clé de chiffrement et activer le mode Wi-Fi :

1. Connectez le téléphone au PC avec un câble USB.
2. Ouvrez une invite de commande (PowerShell) sur le PC et tapez :
   ```powershell
   adb devices
   ```
   *Validez l'autorisation qui apparaît sur l'écran de votre téléphone.*
3. Activez le mode écoute TCP/IP sur le port 5555 :
   ```powershell
   adb tcpip 5555
   ```
4. **Débranchez le câble USB**. Votre téléphone écoute désormais les commandes de synchronisation en Wi-Fi.

---

## 🚀 Utilisation du Script de Synchronisation Wi-Fi
1. Trouvez l'adresse IP de votre téléphone dans les paramètres Wi-Fi de votre appareil (ex: `192.168.1.50`).
2. Ouvrez le fichier de script [2026-07-07_Android_ADB_Sync.py](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/Memoire-Bachelor/03_Travail/Python/2026-07-07_Android_ADB_Sync.py) et modifiez la ligne suivante avec votre adresse IP :
   ```python
   PHONE_IP = "192.168.1.50"
   ```
3. Exécutez le script pour importer sans fil les fichiers audio du smartphone vers le PC :
   ```powershell
   python C:\Users\julien\OneDrive\Bureau\geminicli\Projets\Memoire-Bachelor\03_Travail\Python\2026-07-07_Android_ADB_Sync.py
   ```

---

## 🔁 Fonctionnement de la Synchronisation Globale
Une fois le script d'importation lancé, vos fichiers audio arriveront dans le dossier local du PC. Le démon [2026-07-07_CRM_CubeACR_Sync.py](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/Memoire-Bachelor/03_Travail/Python/2026-07-07_CRM_CubeACR_Sync.py) s'occupera ensuite de :
1. Détecter l'arrivée du fichier audio.
2. Analyser le numéro de téléphone dans le nom du fichier.
3. Déplacer l'enregistrement dans le dossier final `/Audio`.
4. Reconstruire l'interface de votre CRM HTML pour afficher le lecteur audio sur le gîte appelé.
