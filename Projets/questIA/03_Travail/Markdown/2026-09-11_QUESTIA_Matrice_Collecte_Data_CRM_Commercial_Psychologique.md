# Matrice de Collecte Data CRM QuestIA : Intelligence Commerciale & Profilage Psychométrique

> **Document de référence pour l'architecture du CRM QuestIA**  
> **Auteur** : Julien FLORENCE — Director of Strategy & Growth  
> **Périmètre** : Audit Diagnostic Visio (26Q), Cold Calls, Tracking des cibles B2B (Aéronautique, Agro Export, SaaS DeepTech, Équipements Indu, MedTech).

---

## 📋 Checklist & To-Do List des Besoins de Collecte Data (360°)

```
                                  CRM QUESTIA DATA ENGINE (360°)
                                               │
       ┌───────────────────────────────┬───────┴───────────────────────┬───────────────────────────────┐
       ▼                               ▼                               ▼                               ▼
[ DATA FIRMOGRAPHIQUES ]     [ DATA FINANCIÈRES ]            [ DATA DISC / PCM ]            [ GOUVERNANCE & AGENDA ]
• Raison sociale             • CA Export annuel (€)          • Profil DISC (D, I, S, C)      • Validation CSE (Oui/Non)
• Secteur ICP (1 à 5)        • Taux fuite marge (0-5.4%)      • Base PCM (Travaillomane...)   • Périmètre RH vs Secret
• Effectif Sales L2          • Perte net calculée (€/an)     • Canal de communication        • Étape 0 (2 000 € HT)
• Pays acheteurs cibles      • Budget moyen contrat          • Comportement sous stress      • Date de relance visio
```

---

### BLOC 1 : DATA FIRMOGRAPHIQUES & CONTEXTUELLES (Identité Prospect)

- [ ] **ID_01 — Raison Sociale / Nom Entreprise** : Nom légal et nom commercial du prospect.
- [ ] **ID_02 — Secteur ICP Ciblé** :
  - `ICP 1` : Aéronautique & Spatial (Toulouse / Bordeaux)
  - `ICP 2` : Agroalimentaire & Produits de Luxe à l'Export (Vins/Spiritueux, Gastronomie)
  - `ICP 3` : Éditeurs de Logiciels B2B SaaS DeepTech
  - `ICP 4` : Équipements Industriels & Machines Spéciales
  - `ICP 5` : Dispositifs Médicaux & MedTech Export
- [ ] **ID_03 — Volume Force de Vente L2** : Nombre de commerciaux / Account Executives / CSM négociant en langue étrangère (Anglais).
- [ ] **ID_04 — Pays Acheteurs Cibles** : Zones géographiques majeures des acheteurs (US, UK, Asie, Allemagne/Europe du Nord).
- [ ] **ID_05 — Contact Décisionnaire** : Nom, Prénom, Fonction exacte (VP Sales, Directeur Général, DRH, Head of Global Sales).
- [ ] **ID_06 — Coordonnées Directes** : Téléphone mobile direct, Email professionnel, Profil LinkedIn.

---

### BLOC 2 : DATA COMMERCIALES & FINANCIÈRES (Chiffrage Manque à Gagner)

- [ ] **FIN_01 — Chiffre d'Affaires Export Annuel (€)** : CA généré à l'international (ex: 5M€, 15M€, 50M€).
- [ ] **FIN_02 — Taux de Fuite de Marge Mesuré (%)** : Taux de concessions et remises cédées sous la pression de l'acheteur (0% à 5.4%).
- [ ] **FIN_03 — Perte Nette Annuelle Calculée (€/an)** : Formule automatique $\text{CA Export} \times \text{Taux de Fuite}$.
- [ ] **FIN_04 — Valeur Moyenne d'un Contrat (High-Ticket)** : Panier moyen des deals internationaux négociés.
- [ ] **FIN_05 — Type de Concession Majoritaire** :
  - Remise directe de prix sur la ligne de contrat
  - Inclusion gratuite de garanties ou d'options payantes
  - Pénalités de retard ou clauses d'acompte non défendues
- [ ] **FIN_06 — Historique des Pertes de Deals** : Nombre de deals stoppés ou allongés de +40% à cause de blocages de négociation.

---

### BLOC 3 : DATA PSYCHOMÉTRIQUES — MATRICE DISC (Profilage Comportemental)

- [ ] **DISC_01 — Profil DISC Prédominant de l'Acheteur / Prospect** :
  - 🔴 **Dominant (D)** : Orienté résultat, direct, exigeant, réagit aux faits et aux gains rapides.
  - 🟡 **Influent (I)** : Orienté relationnel, enthousiaste, réagit au prestige et à la vision.
  - 🟢 **Stable (S)** : Orienté sécurité, méthodique, réagit aux garanties et à la continuité.
  - 🔵 **Consciencieux (C)** : Orienté procédure, analytique, exige des preuves chiffrées (McKinsey, KPMG).
- [ ] **DISC_02 — Posture de Négociation Ciblée** :
  - Rapport de force agressif / imposition de diktat
  - Retrait tactique / feinte de désintérêt
  - Négociation coopérative / recherche de compromis
- [ ] **DISC_03 — Niveau de Timidité Cultuelle L2** : Taux d'inhibition des commerciaux face au profil DISC du client (mesure du *Foreign-Language Effect*).

---

### BLOC 4 : DATA PROCESS COMMUNICATION MODEL (PCM — Canal & Stress)

- [ ] **PCM_01 — Base PCM Prédominante** :
  - 💼 **Travaillomane** : Organisé, logique, demande des faits et de la structure.
  - 🏛️ **Persévérant** : Observateur, dévoué, évalue selon ses valeurs et ses convictions.
  - ⚡ **Promoteur** : Adaptable, persuasif, recherche l'action et le défi.
  - 🤝 **Empatique** : Chaleureux, sensible, privilégie le climat relationnel.
  - 🎨 **Rebelle** : Spontané, créatif, réagit de façon ludique ou oppositionnelle.
  - 🌌 **Rêveur** : Calme, imaginatif, besoin de temps et de clarté.
- [ ] **PCM_02 — Canal de Communication Privilégié** : Factuel / directif / interrogatif / chaleureux.
- [ ] **PCM_03 — Comportement de Stress Sous Pression** :
  - *Surlavage / Sur-adaptation* (Concession précipitée)
  - *Attaque / Blâme* (Agressivité ou ultimatum)
  - *Création de confusion / Retrait* (Procrastination de closing)

---

### BLOC 5 : DATA GOUVERNANCE & PROCESSUS D'ACHAT

- [ ] **GOV_01 — Statut Consultation CSE** : Le suivi individuel nécessite-t-il une validation du Comité Social et Économique ? (Oui / Non / Non Concerné).
- [ ] **GOV_02 — Confidentialité Souhaitée** : Entraînement vocal confidentiel sans rapport RH vs Tableau de bord RH agrégé.
- [ ] **GOV_03 — Maturation Budgétaire** : Budget de formation / accompagnement disponible (Validation Offre High-Ticket 2 000 € HT / apprenant).
- [ ] **GOV_04 — Étape 0 (Diagnostic Coach 1-sur-1 15 min)** : Statut de réservation (Programmé / En Attente / Réalisé / Validé).
- [ ] **GOV_05 — Horizon Démarrage** : Immédiat (< 15 jours) / Prochain Trimestre / Prochain Exercice.

---

### BLOC 6 : SUIVI COMMERCIAL & TIMELINE ACTION

- [ ] **ACT_01 — Statut Tunnel Prospect** : `Filtre Cold Call` $\rightarrow$ `Visio Audit 30 min (26Q)` $\rightarrow$ `Diagnostic Signé` $\rightarrow$ `Bêta-Testeur Accompagné`.
- [ ] **ACT_02 — Prochaine Action & Date Butoir** : Tâche planifiée de relance personnalisée avec le PDF adapté (#1, #2, #3 ou #4).
- [ ] **ACT_03 — Score de Qualification Globale (0 à 100)** : Indice synthétique d'opportunité High-Ticket.

---

## 🛠️ Schéma de Base de Données JSON (Spécification CRM)

```json
{
  "prospect_id": "QUESTIA-2026-AERO-001",
  "company": {
    "name": "Airbus Subcontracting SAS",
    "sector": "Aéronautique & Spatial",
    "icp_type": "ICP1",
    "export_revenue": 15000000,
    "sales_l2_count": 12,
    "target_countries": ["US", "UK"]
  },
  "contact": {
    "name": "Jean-Claude VASSEUR",
    "title": "VP Commercial & Business Dev",
    "phone": "+33661747573",
    "email": "jc.vasseur@airbus-sub.com"
  },
  "financial_audit": {
    "margin_leak_rate": 4.2,
    "annual_loss_eur": 630000,
    "avg_contract_value": 850000,
    "concession_type": "Garanties offertes & pénalités"
  },
  "psychometrics": {
    "disc_vector": "Dominant (D)",
    "pcm_base": "Travaillomane",
    "stress_behavior": "Attaque directe / Pression tarifaire",
    "persuasion_l2_loss_pct": 30
  },
  "governance": {
    "cse_required": false,
    "privacy_preference": "ENTRAINEMENT_CONFIDENTIEL",
    "etape0_status": "PROGRAMME",
    "offer_ticket_eur": 2000
  }
}
```
