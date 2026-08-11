# -*- coding: utf-8 -*-
"""
Script d'audit et de calcul automatisé des créances salariales — Contentieux Happy House SAS
Convention Collective Nationale de l'Immobilier (IDCC 1527)
"""

def calculer_creances(salaire_brut_mensuel, nb_mois_presence_2025, nb_mois_presence_2026, nb_jours_teletravail_par_semaine=5):
    print("="*65)
    print("AUDIT & CALCUL AUTOMATISÉ DES CRÉANCES SALARIALES - HAPPY HOUSE SAS")
    print("="*65)
    
    # 1. 13e Mois Conventionnel (Art. 38 IDCC 1527)
    creance_13e_2025 = salaire_brut_mensuel * (nb_mois_presence_2025 * 30.5 / 365.0)
    creance_13e_2026 = salaire_brut_mensuel * (nb_mois_presence_2026 * 30.5 / 365.0)
    total_13e = creance_13e_2025 + creance_13e_2026

    # 2. Minima Conventionnels vs SMIC (Art. 37 IDCC 1527)
    minimum_annuel_E1_2025 = 23424.0  # Avenant 104
    minimum_annuel_E1_2026 = 23700.0  # Avenant 110
    
    vers_2025 = salaire_brut_mensuel * nb_mois_presence_2025
    du_2025 = (minimum_annuel_E1_2025 / 12.0) * nb_mois_presence_2025
    ecart_grille_2025 = max(0, du_2025 - vers_2025)

    vers_2026 = salaire_brut_mensuel * nb_mois_presence_2026
    du_2026 = (minimum_annuel_E1_2026 / 12.0) * nb_mois_presence_2026
    ecart_grille_2026 = max(0, du_2026 - vers_2026)
    
    total_ecart_grille = ecart_grille_2025 + ecart_grille_2026

    # 3. Télétravail & Matériel Personnel (Barème URSSAF 2026)
    allocation_tt_mensuel = 11.0 * nb_jours_teletravail_par_semaine  # 55 €/mois pour 5j
    materiel_info_mensuel = 55.20  # Matériel informatique
    occupation_domicile_estimee = 85.00  # Immixtion vie privée (~85 €/mois)
    
    total_mois = nb_mois_presence_2025 + nb_mois_presence_2026
    total_frais_tt = (allocation_tt_mensuel + materiel_info_mensuel + occupation_domicile_estimee) * total_mois

    # Synthèse globale
    total_creances = total_13e + total_ecart_grille + total_frais_tt

    print(f"\n1. Rappel 13e Mois Conventionnel :")
    print(f"   - Période 2025 ({nb_mois_presence_2025} mois) : {creance_13e_2025:.2f} € bruts")
    print(f"   - Période 2026 ({nb_mois_presence_2026} mois) : {creance_13e_2026:.2f} € bruts")
    print(f"   --> Total 13e mois : {total_13e:.2f} € bruts")

    print(f"\n2. Ajustement Minima de Branche (IDCC 1527) :")
    print(f"   - Écart Grille 2025 : {ecart_grille_2025:.2f} € bruts")
    print(f"   - Écart Grille 2026 : {ecart_grille_2026:.2f} € bruts")
    print(f"   --> Total Ajustement Grille : {total_ecart_grille:.2f} € bruts")

    print(f"\n3. Indemnités Télétravail & Occupation Domicile ({total_mois} mois) :")
    print(f"   - Allocation Télétravail ({allocation_tt_mensuel} €/mois) : {allocation_tt_mensuel * total_mois:.2f} €")
    print(f"   - Matériel informatique ({materiel_info_mensuel} €/mois) : {materiel_info_mensuel * total_mois:.2f} €")
    print(f"   - Occupation Domicile ({occupation_domicile_estimee} €/mois) : {occupation_domicile_estimee * total_mois:.2f} €")
    print(f"   --> Total Frais Télétravail : {total_frais_tt:.2f} €")

    print("="*65)
    print(f"💰 TOTAL ESTIMÉ DES CRÉANCES PRINCIPALES : {total_creances:.2f} €")
    print("="*65)
    
    return {
        "total_13e": total_13e,
        "total_ecart_grille": total_ecart_grille,
        "total_frais_tt": total_frais_tt,
        "total_creances": total_creances
    }

if __name__ == "__main__":
    # Paramètres par défaut basés sur le SMIC 2026 (1867 € brut/mois) sur 12 mois d'ancienneté
    calculer_creances(salaire_brut_mensuel=1867.02, nb_mois_presence_2025=6, nb_mois_presence_2026=6)
