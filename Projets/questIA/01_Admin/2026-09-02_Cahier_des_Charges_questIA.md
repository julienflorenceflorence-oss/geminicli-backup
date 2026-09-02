# Projet questIA — Cadre Stratégique & Architecture Power BI

## 📌 Objectif du Projet
Le projet **questIA** vise à développer un tableau de bord analytique et décisionnel de niveau Executive sous **Power BI**, couplant analyse de données d'entreprise et indicateurs de performance d'intégration de l'Intelligence Artificielle.

---

## 🛠️ Architecture du Projet Power BI

### 1. Modélisation des Données (Star Schema)
* **Table de Fais (Fact Table)** : `Fact_Interactions_questIA` (Transactions, requêtes IA, KPIs d'utilisation, coûts, temps de réponse, taux de satisfaction, conversion).
* **Tables de Dimensions (Dimension Tables)** :
  * `Dim_Date` : Calendrier continu (Année, Trimestre, Mois, Semaine, Jour, JourSemaine, EstFérié).
  * `Dim_Utilisateurs` : Segmentation utilisateurs, rôles, départements, niveaux d'adoption.
  * `Dim_Modeles_IA` : Types de modèles utilisés, tokens consommés, taux de précision, coûts/requête.
  * `Dim_Canaux` : Canaux d'accès (Web, App, API, Intégrations).

### 2. Bibliothèque de Mesures DAX (À développer)
* **Volume & Utilisation** : Nombre total d'interactions, utilisateurs actifs mensuels (MAU) / quotidiens (DAU).
* **Coûts & ROI** : Coût cumulé des appels IA, coût moyen par session, ROI estimé sur le temps gagné.
* **Temps & Performance (Time Intelligence)** : Évolution MoM (Month-over-Month), YoY (Year-over-Year), Cumul Annuel YTD (Year-to-Date).

---

## 📂 Structure des Fichiers du Projet
- `01_Admin/` : Cahier des charges et spécifications.
- `02_Sources/` : Données brutes (CSV, Excel, exports API).
- `03_Travail/` :
  - `/PowerQuery/` : Scripts M de nettoyage et transformation.
  - `/DAX/` : Formules et bibliothèque de mesures DAX.
  - `/Markdown/` : Notes d'architecture et de conception.
- `04_Livrables/` : Documentation utilisateur et synthèses décisionnelles.
- `05_Archives/` : Versions antérieures.
