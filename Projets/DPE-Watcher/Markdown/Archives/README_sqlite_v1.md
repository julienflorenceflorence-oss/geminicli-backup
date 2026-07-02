# 🎯 DPE Watcher - Outil Automatisé de Veille ADEME (100% Gratuit)

DPE Watcher est une solution Python légère et robuste, conçue pour récupérer quotidiennement les nouveaux Diagnostics de Performance Énergétique (DPE) publiés par l'ADEME, filtrer les résultats sur des codes postaux cibles, éliminer les doublons grâce à un historique local SQLite, puis générer un fichier Excel d'exportation stylisé (style "Édition Prestige") envoyé automatiquement par email.

Cette solution est **100% gratuite**, sans aucun frais d'infrastructure Cloud ou d'API payante.

---

## 📂 Structure du Projet

Conformément aux normes d'organisation du poste de travail :
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
│   ├── dpe_watcher.py             <- Script principal d'automatisation
│   ├── config.json                <- Fichier de paramètres (codes postaux, SMTP, etc.)
│   ├── requirements.txt           <- Dépendances Python requises
│   ├── test_installation.py       <- Script de diagnostic d'installation
│   ├── run_dpe_watcher.bat        <- Script de lancement pour le planificateur de tâches
│   └── Archives/                  <- Versions archivées du code source
└── Data/
    ├── dpe_history.db             <- Base SQLite contenant l'historique des DPE déjà traités
    └── dpe_watcher.log            <- Journal d'exécution (logs)
```

---

## 🛠️ Instructions d'Installation

### 1. Prérequis
- **Python 3.12+** installé sur votre machine. Assurez-vous d'avoir coché l'option *"Add Python to PATH"* lors de l'installation.
- Un serveur ou un compte e-mail avec accès SMTP (ex: Gmail avec mot de passe d'application, Brevo, SFR, Orange, ou votre serveur d'entreprise).

### 2. Création de l'environnement et installation
Ouvrez votre terminal (PowerShell ou Invite de commandes) dans le dossier `Projets/DPE-Watcher/Python` :

```powershell
# 1. Se déplacer dans le dossier Python
cd "C:\Users\julien\OneDrive\Bureau\geminicli\Projets\DPE-Watcher\Python"

# 2. Créer un environnement virtuel isolé (recommandé)
python -m venv .venv

# 3. Activer l'environnement virtuel
# Sur Windows :
.venv\Scripts\activate

# 4. Installer les dépendances requises (pandas, openpyxl, requests)
pip install -r requirements.txt
```

### 3. Exécution du diagnostic d'installation
Pour valider que tout est correctement installé et que votre machine peut se connecter à l'API ADEME, lancez :
```powershell
python test_installation.py
```
Le diagnostic doit valider que les modules sont présents, que SQLite fonctionne et que la connexion vers `data.ademe.fr` est établie.

---

## ⚙️ Configuration du fichier `config.json`

Ouvrez le fichier `config.json` présent dans le dossier `/Python` et modifiez les paramètres selon vos besoins :

```json
{
  "ademe_api": {
    "datasets": [
      {
        "id": "meg-83tjwtg8dyz4vv7h1dqe",
        "name": "Logements existants"
      },
      {
        "id": "g3cgx7jb3cmys5voxz1mrm22",
        "name": "Logements neufs"
      }
    ],
    "days_to_check": 7,                  // Fenêtre d'interrogation en arrière (en jours)
    "request_timeout_seconds": 30
  },
  "filtering": {
    "codes_postaux": [
      "11000",                           // Remplacer par vos codes postaux cibles
      "11100",
      "31000"
    ]
  },
  "email": {
    "smtp_server": "smtp.gmail.com",     // Votre serveur SMTP (ex: smtp.gmail.com ou smtp-relay.brevo.com)
    "smtp_port": 587,                    // Port standard (587 pour TLS, 465 pour SSL)
    "smtp_username": "votre.email@gmail.com",
    "smtp_password": "xxxx xxxx xxxx xxxx", // Mot de passe d'application (Gmail) ou clé SMTP
    "use_tls": true,
    "use_ssl": false,
    "from_email": "votre.email@gmail.com",
    "to_emails": [
      "destinataire@example.com"         // Liste des destinataires de l'export Excel
    ],
    "subject_prefix": "[DPE Watcher]",
    "send_email_if_empty": false         // Envoyer un email même s'il n'y a aucun nouveau DPE ? (conseillé: false)
  }
}
```

> [!TIP]
> **Sécurité Gmail (SMTP) :** Si vous utilisez une adresse Gmail comme expéditeur, vous devez activer la double authentification sur votre compte Google, puis générer un **Mot de passe d'application** spécifique (Rubrique Sécurité > Connexion à Google > Mots de passe d'application). Utilisez ce mot de passe à 16 caractères sans espaces dans le champ `smtp_password`.

---

## 🚀 Automatisation quotidienne sous Windows

Pour exécuter le script tous les jours de façon transparente et gratuite, nous utilisons le **Planificateur de tâches de Windows (Task Scheduler)**.

### Configuration pas-à-pas :
1. Ouvrez le menu Démarrer, tapez **Planificateur de tâches** et ouvrez-le.
2. Dans le panneau de droite, cliquez sur **Créer une tâche de base...**.
3. **Nom** : Saisissez `DPE Watcher - Veille ADEME`. Cliquez sur Suivant.
4. **Déclencheur** : Sélectionnez **Tous les jours**. Cliquez sur Suivant. Saisissez l'heure d'exécution souhaitée (par exemple 08:30 chaque matin).
5. **Action** : Sélectionnez **Démarrer un programme**. Cliquez sur Suivant.
6. **Programme/script** : Cliquez sur Parcourir et sélectionnez le fichier batch :
   `C:\Users\julien\OneDrive\Bureau\geminicli\Projets\DPE-Watcher\Python\run_dpe_watcher.bat`
7. **Commencer dans (facultatif)** : Indiquez le chemin absolu du dossier Python (indispensable pour la résolution des chemins relatifs) :
   `C:\Users\julien\OneDrive\Bureau\geminicli\Projets\DPE-Watcher\Python\`
8. Cliquez sur Suivant puis sur **Terminer**.

Désormais, Windows lancera de manière transparente le script tous les jours à l'heure choisie.

---

## 📊 Fonctionnement & Élimination des Doublons

1. **Historique local (SQLite) :** Lors du premier lancement, le dossier `Data/` et la base `dpe_history.db` sont initialisés. Chaque nouveau DPE extrait de l'API ADEME y est stocké avec sa clé unique `numero_dpe`.
2. **Requête API optimisée :** Le script interroge l'API ADEME en filtrant sur la période (par exemple les 7 derniers jours). Cela permet de capter les DPE qui ont été validés ou téléversés avec du retard par le diagnostiqueur.
3. **Déduplication robuste :** Le script compare les DPE récupérés avec ceux déjà enregistrés en base locale. Seuls les DPE n'ayant jamais été traités sont exportés et stockés.
4. **Export prestige :** Les nouvelles données sont enregistrées dans `04_Livrables/Data/DPE_Nouveaux.xlsx` avec un design raffiné (en-tête noir profond `#0F1115`, ligne inférieure dorée `#D4AF37`, texte doré, alternance de lignes discrète et ajustement automatique de colonnes).
5. **Versioning binaire :** Avant de réécrire le fichier Excel actif `DPE_Nouveaux.xlsx`, l'ancienne version est automatiquement renommée avec la date et l'heure (ex: `DPE_Nouveaux_2026-07-02_083000.xlsx`) et stockée dans le sous-dossier `Archives/`.

---

## 📝 Consultation des Logs
En cas de problème (panne d'Internet, erreur SMTP, API ADEME hors-ligne), vous pouvez consulter le fichier de log situé à cette adresse :
`C:\Users\julien\OneDrive\Bureau\geminicli\Data\dpe_watcher.log`

Il contient le détail chronologique de chaque exécution et trace les éventuelles erreurs pour simplifier le diagnostic.
