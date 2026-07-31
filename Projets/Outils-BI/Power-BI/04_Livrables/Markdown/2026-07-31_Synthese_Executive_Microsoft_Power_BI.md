# 📊 Guide d'Excellence & Synthèse Stratégique : Microsoft Power BI

Ce document présente une **analyse complète et structurée de Microsoft Power BI**, ses composants d'architecture, ses moteurs d'analyse (Power Query & DAX), ses **cas d'usage métier** (Management, P&L, Vente & Hôtellerie/CHR) et la feuille de route de certification **Microsoft PL-300**.

---

## 🏛️ 1. Qu'est-ce que Microsoft Power BI ?

**Microsoft Power BI** est la plateforme cloud de référence mondiale en **Business Intelligence (BI)** et **Data Visualization**, classée leader incontesté au *Gartner Magic Quadrant* depuis plus de 8 ans.

Sa mission est de transformer des volumes de données brutes disséminées (fichiers Excel, bases SQL, CRM Bitrix24/Salesforce, ERP, fichiers CSV, APIs Web) en **tableaux de bord interactifs, visuels et automatisés**, facilitant la prise de décision stratégique en temps réel.

```
[ Sources Brutes ] ──► [ Power Query (ETL) ] ──► [ Modèle en Étoile ] ──► [ DAX & Visuals ] ──► [ Décision Business ]
 (Excel, SQL, CRM)      (Nettoyage & M Code)     (Fact & Dimensions)     (Mesures & KPIs)        (Dashboards Cloud)
```

---

## ⚙️ 2. L'Architecture en 4 Composants Clés

| Composant | Rôle & Usage | Utilisateurs Cibles |
| :--- | :--- | :--- |
| **Power BI Desktop** | Application Windows gratuite de création de modèles de données, calculs DAX et rapports visuels. | Data Analyst, Manager, Concepteur BI |
| **Power BI Service (Cloud SaaS)** | Plateforme cloud sécurisée pour publier, partager les tableaux de bord et programmer les rafraîchissements auto. | Dirigeants, Managers, Équipes opérationnelles |
| **Power BI Mobile** | Application iOS & Android optimisée pour la consultation de KPIs sur smartphone ou tablette en déplacement. | Cadres nomades, Directeurs de site |
| **Power BI Embedded / Fabric** | Intégration transparente de rapports au cœur d'outils métiers (CRM, Intranet, Applications SaaS). | Développeurs, DSI |

---

## 🛠️ 3. Les 3 Moteurs Techniques Fondamentaux

### A. Power Query & Langage M (L'Étape ETL)
C'est le moteur d'**Extraction, Transformation et Chargement (ETL)**.
* **Fonctions clés** : Nettoyage des valeurs NULL/erreurs, suppression des doublons, fusion de tables (Merge), ajout de requêtes (Append) et **dépivotage des colonnes (Unpivot)** pour rendre les données lisibles par le moteur analytique.
* *Règle d'or* : Effectuer le maximum de transformations en amont dans Power Query plutôt que de surcharger le langage DAX.

### B. Modélisation de Données (Le Modèle en Étoile / Star Schema)
Un rapport performant repose sur une architecture claire :
* **Tables de Faits (Fact Tables)** : Contiennent les données numériques et transactions (ex: *Ventes de la veille, Lignes de factures, Consommations F&B*).
* **Tables de Dimensions (Dim Tables)** : Contiennent les attributs de contexte (ex: *Table Dates/Calendrier, Table Clients, Table Produits, Table Établissements*).
* **Cardinalité** : Relations de 1 à N ($1:*$) entre les dimensions et la table de faits.

### C. Le Langage DAX (Data Analysis Expressions)
DAX est le langage de formules analytiques pour créer des calculs complexes et des mesures dynamiques :
* **Calcul du Contexte (`CALCULATE`)** : La fonction reine pour modifier le contexte de filtre.
  ```dax
  CA_Rooftop = CALCULATE(SUM(Ventes[Montant]), Dimensions[Pôle] = "Rooftop")
  ```
* **Intelligence Temporelle (Time Intelligence)** : Comparaison automatique d'une période à l'autre.
  ```dax
  CA_N_minus_1 = CALCULATE(SUM(Ventes[Montant]), SAMEPERIODLASTYEAR('Calendrier'[Date]))
  CA_Cumul_YTD = TOTALYTD(SUM(Ventes[Montant]), 'Calendrier'[Date])
  ```
* **Ratios de Rentabilité (Division Sécurisée)** :
  ```dax
  Food_Cost_Pct = DIVIDE(SUM(Achats[Cout_Matiere]), SUM(Ventes[CA_Nourriture]), 0)
  ```

---

## 📈 4. Cas d'Usage Métier Concrets pour Julien Florence

### 📊 Cas 1 : Cockpit de Pilotage Financier & P&L (Direction Général & CHR)
* **Visualisations** : Cartes KPI (Chiffre d'Affaires, EBITDA %), graphique en cascade (Waterfall) pour visualiser la décomposition des charges, et jauge de suivi du budget.
* **KPIs Clés** :
  * CA Hébergement vs CA F&B.
  * Prime Cost % (Masse Salariale + Coût Matière).
  * Évolution YoY du résultat net.

### 🎯 Cas 2 : Dashboard Performance Commerciale & CRM (Sales & Smarketing)
* **Visualisations** : Entonnoir de conversion (Funnel), graphique à barres croisées par commercial, carte thermique géographique des clients.
* **KPIs Clés** :
  * Taux de conversion des opportunités CRM (Bitrix24).
  * Panier moyen et cycle de vente moyen en jours.
  * Atteinte des objectifs par vendeur.

### 🏨 Cas 3 : Dashboard Hôtellerie Hybride (RevPAR & Exploitation Site)
* **Visualisations** : Courbes de suivi du taux d'occupation par type de chambre (chambre Signature vs lits dortoirs), matrice de captage F&B.
* **KPIs Clés** :
  * RevPAR (Revenue Per Available Room) et ADR (Average Daily Rate).
  * RevPAG (CA Total par client présent).
  * Part du canal de réservation directe vs OTAs (Booking/Airbnb).

---

## 🎓 5. Feuille de Route Certification Microsoft PL-300

Pour valoriser cette expertise d'analyse de données auprès des recruteurs et des directions générales, la certification visée est :  
🏆 **Microsoft Certified: Power BI Data Analyst Associate (Examen PL-300)**

### Les 4 Piliers de l'Examen PL-300 :
1. **Préparer les données** (25–30%) — Power Query, M Code, Connexions.
2. **Modéliser les données** (25–30%) — Modèle en étoile, DAX, Rôles RLS.
3. **Visualiser et analyser les données** (25–30%) — Graphiques, Drill-down, Storytelling.
4. **Gérer et sécuriser les livrables** (15–20%) — Power BI Service, Espaces de travail, Rafraîchissements.
