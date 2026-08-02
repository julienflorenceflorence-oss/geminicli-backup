# 🎯 DPE Watcher Premium - Veille ADEME & Google Sheets (100% Gratuit)

DPE Watcher Premium est une solution automatisée haut de gamme conçue pour surveiller quotidiennement les nouveaux Diagnostics de Performance Énergétique (DPE) de l'ADEME, filtrer les résultats sur des codes postaux précis, dédupliquer les entrées via une feuille **Google Sheets** partagée, puis générer et envoyer un export Excel Premium (style "Édition Prestige") par email.

Cette architecture est entièrement **gratuite** et conçue pour être **facilement transférable** à un tiers (client ou collaborateur).

---

## 📂 Structure du Projet

```text
Projets/DPE-Watcher/
├── 01_Admin/
├── 02_Sources/
├── 03_Travail/
├── 04_Livrables/
│   └── Data/                      <- Contient le fichier Excel actif envoyé par e-mail
│       ├── DPE_Nouveaux.xlsx      <- Fichier Excel actif en cours (sans suffixe de version)
│       └── Archives/              <- Historique des exports Excel envoyés (avec horodatage)
├── 05_Archives/
├── Python/
│   ├── dpe_watcher.py             <- Script principal d'extraction et de communication
│   ├── google_apps_script.js      <- Code JavaScript à copier dans le Google Sheet
│   ├── config.json                <- Fichier de paramètres (codes postaux, SMTP, URL Sheet...)
│   ├── requirements.txt           <- Dépendances Python requises (requests, pandas, openpyxl)
│   ├── test_installation.py       <- Script de diagnostic d'installation et de connexion
│   ├── run_dpe_watcher.bat        <- Script de lancement pour le planificateur de tâches Windows
│   └── Archives/                  <- Versions archivées du code source
└── Data/
    ├── dpe_watcher.log            <- Journal d'exécution (logs de l'outil)
    └── Archives/
```

---

## ⚙️ Étape 1 : Configuration du Google Sheet (Base de Données)

Le script utilise Google Sheets comme base de données pour stocker l'historique de déduplication et pour permettre une consultation humaine en direct.

1. Créez un nouveau document **Google Sheets** sur votre compte Google.
2. Ouvrez le document, puis allez dans le menu supérieur **Extensions** > **Apps Script**.
3. Supprimez tout code existant dans l'éditeur et collez le contenu du fichier [google_apps_script.js](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/google_apps_script.js).
4. Cliquez sur l'icône de disquette (**Enregistrer**).
5. Cliquez sur le bouton bleu **Déployer** (en haut à droite) > **Nouveau déploiement**.
6. Sélectionnez le type de déploiement en cliquant sur l'icône d'engrenage > **Application Web**.
7. Remplissez les paramètres ainsi :
   - **Description :** `DPE Watcher API`
   - **Exécuter en tant que :** `Moi (votre adresse email)`
   - **Qui a accès :** `Tous (ou Anyone)` *(Indispensable pour que le script Python puisse communiquer avec lui)*.
8. Cliquez sur **Déployer**. Google va vous demander d'autoriser les accès. Cliquez sur *Autoriser l'accès*, puis sur *Paramètres avancés* (en bas à gauche) et sur *Accéder à Projet sans titre (non sécurisé)*, puis validez.
9. Copiez l'**URL de l'application Web** fournie (elle se termine par `/exec`). Elle ressemble à ceci :
   `https://script.google.com/macros/s/XXXXXX_XXXXXX/exec`

---

## 🛠️ Étape 2 : Installation du script local

1. Ouvrez votre console Windows (PowerShell ou Invite de commandes) dans le dossier du projet :
   ```powershell
   cd "C:\Users\julien\OneDrive\Bureau\geminicli\Projets\DPE-Watcher\Python"
   ```
2. Créez et activez un environnement virtuel Python :
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Installez les dépendances :
   ```powershell
   pip install -r requirements.txt
   ```
4. Ouvrez le fichier [config.json](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/config.json) et :
   - Renseignez l'URL récupérée à l'Étape 1 dans la clé `"web_app_url"`.
   - Modifiez vos codes postaux sous `"codes_postaux"`.
   - Configurez vos identifiants d'envoi SMTP (Gmail, Brevo, etc.) sous `"email"`.
5. Validez l'installation et les connexions réseau en exécutant le script de diagnostic :
   ```powershell
   python test_installation.py
   ```

---

## 🚀 Étape 3 : Planification quotidienne Windows

Pour que l'outil s'exécute automatiquement chaque matin :
1. Lancez le **Planificateur de tâches** Windows.
2. Créez une **Tâche de base** nommée `DPE Watcher`.
3. Déclencheur : **Tous les jours** à l'heure de votre choix (ex : 08:30).
4. Action : **Démarrer un programme**.
5. Programme/script : Sélectionnez le fichier [run_dpe_watcher.bat](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/run_dpe_watcher.bat).
6. **Commencer dans :** Renseignez absolument le chemin absolu du dossier Python :
   `C:\Users\julien\OneDrive\Bureau\geminicli\Projets\DPE-Watcher\Python\`

---

## 📦 Procédure de passation à un tiers (Option de transfert Gmail dédié)

Puisque cet outil est destiné à une tierce personne, voici la marche à suivre pour lui remettre les clés de l'administration complète :

1. **Création de la boîte mail projet :** Créez une adresse Gmail neutre (ex : `dpe.watcher.client@gmail.com`).
2. **Propriété Google Sheet :** 
   - Créez le Google Sheet sur cette boîte mail.
   - Si vous l'avez créé sur votre compte personnel, partagez-le avec l'adresse du client et nommez-le **Propriétaire** (Owner).
   - Ouvrez Apps Script sur le compte du client, et effectuez le déploiement (Étape 1) pour obtenir une URL de Web App rattachée à son compte. Renseignez cette URL dans le `config.json` final.
3. **Propriété GitHub :** Invitez le compte GitHub du tiers (`https://github.com/...`) en tant que collaborateur ou transférez-lui directement le dépôt privé.
4. **Remise des identifiants :** Donnez-lui le mot de passe de la boîte Gmail projet (qui lui permettra d'accéder au Google Sheet, à Render, à Brevo et à GitHub).
5. **Configuration locale finale :** Le tiers devra simplement installer Python, configurer ses propres destinataires mails dans le `config.json` et activer le Planificateur de Tâches Windows sur sa machine de travail.
