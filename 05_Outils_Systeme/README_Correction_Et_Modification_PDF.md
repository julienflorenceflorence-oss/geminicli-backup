# 🛠️ Guide de Modification Directe des Textes sans Altérer le Design

Ce guide explique les **3 méthodes simples et rapides** pour modifier le texte de vos CVs et documents PDF (JOST, Athéna, etc.) sans risque de déformer la mise en page, les boutons, les couleurs ou la structure A4.

---

## ⚡ Méthode 1 : Demande Directe à l'IA (La méthode 100% Automatisée)

C'est la méthode la plus simple et sans aucun risque d'erreur :
* Vous me donnez la consigne exacte dans le chat (ex: *"Remplace telle phrase par telle phrase"*).
* Antigravity exécute le script de régénération vectorielle (`05_Outils_Systeme/generate_exact_replica_cv_pdf.py`).
* Le PDF et le fichier HTML sont mis à jour **en 5 secondes** sur votre Bureau Mac et sur GitHub, en préservant 100% du design Sombre & Or, de la photo et des boutons cliquables.

---

## 🌐 Méthode 2 : Édition du Fichier HTML Source (100% Maîtrise Visuelle)

Votre projet contient toujours les fichiers source HTML d'origine :
* **Emplacement** : `Projets/prospection job/jost-hotel-bordeaux/04_Livrables/HTML/2026-07-31_CV_Julien_Florence_JOST_Bordeaux.html`
* **Procédure** :
  1. Ouvrez le fichier `.html` avec n'importe quel éditeur de texte (VS Code, TextEdit).
  2. Modifiez le texte souhaité entre les balises HTML.
  3. Ouvrez le fichier dans **Google Chrome** ou **Safari**.
  4. Faites `Imprimer (Cmd + P)` ➔ `Enregistrer au format PDF`.
  *La mise en page CSS, les boutons arrondis et les couleurs resteront strictement identiques.*

---

## 📄 Méthode 3 : Logiciels d'Édition PDF Directe (Sans Toucher au Code)

Si vous souhaitez modifier le PDF directement à la souris sur votre poste :
1. **PDFgear** (Logiciel Gratuit sur Mac & Windows) :
   - Ouvrez le PDF dans PDFgear ➔ Cliquez sur **« Éditer le texte »** ➔ Modifiez les mots directement sur le document.
2. **Adobe Acrobat Pro** ou **Canva** :
   - Importez le fichier PDF dans Canva ou Acrobat Pro. Les zones de texte deviennent modifiables à la volée tout en conservant les vecteurs et le style graphique.
