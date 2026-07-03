# 🎯 DPE Watcher Premium - Version Sécurisée & Exécutable (Anti-Copie)

DPE Watcher Premium est une solution automatisée haut de gamme conçue pour surveiller quotidiennement les nouveaux Diagnostics de Performance Énergétique (DPE) de l'ADEME, filtrer les résultats sur des codes postaux précis, dédupliquer les entrées via une feuille **Google Sheets** partagée, puis générer et envoyer un export Excel Premium (style "Édition Prestige") par email.

Cette version intègre des **mécanismes de protection de propriété intellectuelle (sécurisation du code source et binaire)** pour empêcher la copie ou la modification non autorisée de la part du client ou d'un utilisateur final.

---

## 📂 Structure du Projet Sécurisé

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
│   ├── dpe_watcher.exe            <- L'exécutable autonome compilé (Code Python caché)
│   ├── dpe_watcher.py             <- Script principal (Pour administration interne uniquement)
│   ├── google_apps_script.js      <- Code JavaScript à copier dans le Google Sheet
│   ├── config.json                <- Fichier de paramètres (codes postaux, SMTP, URL Sheet...)
│   ├── requirements.txt           <- Dépendances Python requises
│   ├── test_installation.py       <- Script de diagnostic d'installation et de connexion
│   ├── run_dpe_watcher.bat        <- Script de lancement pour le planificateur Windows
│   └── Archives/                  <- Versions archivées du code source
├── HTML/
│   ├── dashboard.html             <- Dashboard Externe protégé (Anti-Sélection / Anti-Clic Droit / Anti-F12)
│   └── Archives/                  <- Versions archivées du Dashboard
└── Data/
    ├── dpe_watcher.log            <- Journal d'exécution (logs de l'outil)
    └── Archives/
```

---

## 🔒 Étape 1 : Protection du Code Source

Pour protéger le travail et empêcher le client de récupérer ou copier la logique métier :

### 1. Le Robot d'extraction Python (`dpe_watcher.exe`)
Le script de surveillance [dpe_watcher.py](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/dpe_watcher.py) a été compilé en un **exécutable binaire Windows autonome** : **[dpe_watcher.exe](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/dpe_watcher.exe)**.
- Le code source Python est encapsulé sous forme compilée et ne peut pas être lu ni copié.
- Le client n'a plus besoin d'installer Python, ni d'activer un environnement virtuel `.venv`, ni d'exécuter de commandes `pip`. Il double-clique simplement sur le fichier `.exe` (ou via le `.bat`).
- Le programme va charger le fichier `config.json` externe placé à côté de lui pour la configuration (SMTP, codes postaux, etc.).

### 2. Le Dashboard HTML Premium (`dashboard.html`)
Le fichier **[dashboard.html](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/HTML/dashboard.html)** intègre plusieurs niveaux de sécurisation pour décourager 99 % des utilisateurs d'accéder au code JavaScript :
- **Anti-Sélection :** Désactivation de la sélection textuelle sur toute la page (`user-select: none`).
- **Anti-Clic Droit :** Le menu contextuel est bloqué (`contextmenu` désactivé) pour empêcher l'accès au menu "Inspecter" ou "Afficher le code source de la page".
- **Anti-Raccourcis Clavier :** Interception et blocage des touches de développement standard :
  - `F12` (Outils de développement)
  - `Ctrl + Shift + I` et `Ctrl + Shift + J` (Console et inspecteur)
  - `Ctrl + U` (Affichage du code source natif du navigateur)
- **Minification et obfuscation des variables :** Les variables globales sensibles et les fonctions clés du script ont été renommées sous des noms compacts et opaques (ex: `rawData` -> `_dData`, `filteredData` -> `_fData`, `fetchData` -> `_getData`, etc.) pour dissimuler la logique d'interrogation de l'API Sheets.

---

## 🎨 Étape 2 : Consultation du Dashboard Externe Premium

1. Allez dans le dossier du projet : `Projets/DPE-Watcher/HTML/`
2. Double-cliquez sur le fichier **[dashboard.html](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/HTML/dashboard.html)**. Il s'ouvrira directement dans votre navigateur (Chrome, Edge, etc.) sans nécessiter d'installation.
3. Lors de la première ouverture, cliquez sur le bouton **🔑 Configuration** en haut à droite, collez l'**URL de la Web App** Google Sheets obtenue à l'Étape 1, puis cliquez sur **Sauvegarder**.
4. Le Dashboard va charger et afficher instantanément :
   - **Vos indicateurs de prospection :** Nombre de passoires thermiques, quantité de DPE critiques (G et F), surface habitable moyenne.
   - **Graphiques interactifs :** Répartition complète des classes énergétiques de A à G, et répartition par type de bâtiment (Maisons vs Appartements).
   - **Registre des diagnostics :** Tableau de tous les DPE, triable sur toutes les colonnes, avec un filtre de recherche instantané par commune et par code postal.
   - **Exportateur de données :** Un bouton **📤 Export CSV** pour télécharger immédiatement les DPE filtrés dans un fichier exploitable.

---

## 🛠️ Étape 3 : Configuration du Google Sheet (Base de Données)

Le script utilise Google Sheets comme base de données et comme tableau de bord visuel interactif.

1. Créez un nouveau document **Google Sheets** sur votre compte Google.
2. Ouvrez le document, puis allez dans le menu supérieur **Extensions** > **Apps Script**.
3. Supprimez tout code existant dans l'éditeur et collez le contenu du fichier [google_apps_script.js](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/google_apps_script.js).
4. Cliquez sur l'icône de disquette (**Enregistrer**).
5. Cliquez sur le bouton bleu **Déployer** (en haut à droite) > **Nouveau déploiement**.
6. Sélectionnez le type de déploiement en cliquant sur l'icône d'engrenage > **Application Web**.
7. Remplissez les paramètres ainsi :
   - **Description :** `DPE Watcher API & Dashboard`
   - **Exécuter en tant que :** `Moi (votre adresse email)`
   - **Qui a accès :** `Tous (ou Anyone)` *(Indispensable pour la liaison API)*.
8. Cliquez sur **Déployer** et validez les autorisations d'accès de votre compte.
9. Copiez l'**URL de l'application Web** fournie (se terminant par `/exec`).

---

## 🚀 Étape 4 : Planification bi-quotidienne Windows (7j/7)

Pour configurer une vérification automatique **le matin à 07h00** et **le soir à 23h55** :

1. Ouvrez le **Planificateur de tâches** Windows (Task Scheduler).
2. Dans le panneau de droite, cliquez sur **Créer une tâche...** (et non une tâche de base).
3. **Onglet Général :** Nommez la tâche `DPE Watcher - Veille ADEME`. Sélectionnez *Exécuter même si l'utilisateur n'est pas connecté* et cochez *Exécuter avec les autorisations les plus élevées*.
4. **Onglet Déclencheurs :** Cliquez sur **Nouveau...** :
   - **Déclencheur 1 (Matin) :** Sélectionnez *Chaque jour*, réglez l'heure sur **07:00:00**, répétez tous les 1 jours, cochez *Activé*.
   - **Déclencheur 2 (Soir) :** Cliquez à nouveau sur *Nouveau...*, sélectionnez *Chaque jour*, réglez l'heure sur **23:55:00**, cochez *Activé*.
5. **Onglet Actions :** Cliquez sur **Nouveau...** > Démarrer un programme > Sélectionnez le fichier batch :
   `C:\Users\julien\OneDrive\Bureau\geminicli\Projets\DPE-Watcher\Python\run_dpe_watcher.bat`
   - *Commencer dans :* Indiquez le chemin absolu du dossier Python :
     `C:\Users\julien\OneDrive\Bureau\geminicli\Projets\DPE-Watcher\Python\`
6. **Onglet Conditions :** Décochez *Démarrer la tâche uniquement si l'ordinateur est alimenté par secteur*.
7. Cliquez sur **OK** et saisissez votre mot de passe de session.

---

## 📦 Procédure de livraison sécurisée au client final

Pour remettre le produit à ton client tout en bloquant l'accès au code source :

1. **Fichiers à lui donner :**
   Créez une archive ZIP contenant uniquement :
   - Le fichier [dpe_watcher.exe](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/dpe_watcher.exe) (sans le fichier `dpe_watcher.py` !).
   - Le fichier [config.json](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/config.json).
   - Le fichier [run_dpe_watcher.bat](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/Python/run_dpe_watcher.bat).
   - Le dossier `HTML/` avec uniquement [dashboard.html](file:///C:/Users/julien/OneDrive/Bureau/geminicli/Projets/DPE-Watcher/HTML/dashboard.html).
   - L'arborescence des dossiers vide (avec uniquement les dossiers `01_Admin`, `02_Sources`, `03_Travail`, `04_Livrables/Data`, `05_Archives`, `Data/`).
2. **Propriété Google Sheets :**
   - Créez le Google Sheet final sur le compte Google du client.
   - Installez-y le code Apps Script et activez le déploiement. Renseignez l'URL finale dans le `config.json` et dans le Dashboard.
   - De cette façon, le client a son propre Google Sheets autonome, mais il n'a jamais accès à la logique d'extraction ADEME (qui est cachée dans le `.exe` local) ni au code source du Dashboard HTML (qui est protégé contre l'inspection).
