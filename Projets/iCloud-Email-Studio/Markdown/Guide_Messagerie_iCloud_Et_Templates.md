# ☁️ Guide de Configuration Messagerie iCloud & Templates Style GitHub

Ce guide formalise l'utilisation de votre adresse e-mail **iCloud** (`@icloud.com`, `@me.com` ou `@mac.com`) pour envoyer des e-mails professionnels au design élégant inspiré du **GitHub Design System** (badges, tableaux, alertes `> [!NOTE]`, thèmes sombre et clair).

---

## 🚀 Vue d'Ensemble des 2 Méthodes d'Envoi

| Méthode | Usage recommandé | Prérequis |
| :--- | :--- | :--- |
| **Méthode 1 : Copier-Coller Direct (Apple Mail)** | Utilisation quotidienne sur Mac/iPhone | Aucun (utilise l'application Mail du Mac) |
| **Méthode 2 : Envoi Automatisé (Script Python SMTP)** | Envois automatisés ou programmés | Mot de passe d'application Apple ID |

---

## 📌 Méthode 1 : Copier-Coller dans Apple Mail (Recommandée sur Mac)

Le Studio Web inclut un moteur **CSS Inliner** qui convertit automatiquement le style GitHub pour le rendre 100% compatible avec l'application Apple Mail et iCloud Webmail.

### Étapes :
1. Lancez l'application web en ouvrant le fichier [`Projets/iCloud-Email-Studio/HTML/index.html`](file:///Users/admin/Desktop/geminicli-backup/Projets/iCloud-Email-Studio/HTML/index.html) dans votre navigateur.
2. Choisissez un modèle ou rédigez votre texte en Markdown.
3. Cliquez sur le bouton vert **`Copier dans Apple Mail`** (en haut à droite).
4. Ouvrez **Apple Mail** (ou icloud.com/mail) et créez un nouveau message.
5. Effectuez un **`Cmd + V` (Coller)** dans le corps du message.
   * *Résultat* : Votre e-mail s'affiche instantanément avec l'exact rendu GitHub (couleurs, cartes, alertes, tableaux, boutons).

---

## 🔐 Méthode 2 : Envoi via le Script Python & SMTP iCloud

Pour des envois automatisés ou intégrés à des scripts, vous pouvez utiliser le serveur SMTP officiel d'Apple : `smtp.mail.me.com:587`.

> [!IMPORTANT]
> **Sécurité Apple ID (Double Authentification)** : Apple interdit l'utilisation de votre mot de passe principal pour la connexion SMTP. Vous **devez** générer un **Mot de Passe Spécifique à une Application**.

### Étape 1 : Générer un Mot de Passe d'Application Apple
1. Connectez-vous sur votre compte Apple : **[appleid.apple.com](https://appleid.apple.com)**.
2. Allez dans le menu **Connexion et sécurité**.
3. Sélectionnez **Mots de passe spécifiques à une application**.
4. Cliquez sur **Générer un mot de passe spécifique à une application...**.
5. Donnez un nom à l'application (ex: `Email Studio`) et validez avec votre code 2FA.
6. Copiez le mot de passe généré (format : `xxxx-xxxx-xxxx-xxxx`).

### Étape 2 : Lancer le script d'envoi Python
Utilisez le script autonome situé dans [`Projets/iCloud-Email-Studio/Python/send_icloud_email.py`](file:///Users/admin/Desktop/geminicli-backup/Projets/iCloud-Email-Studio/Python/send_icloud_email.py).

```bash
python3 Projets/iCloud-Email-Studio/Python/send_icloud_email.py \
  --from "votre-adresse@icloud.com" \
  --to "destinataire@exemple.com" \
  --subject "🚀 Compte-Rendu Stratégique" \
  --html-file "Projets/iCloud-Email-Studio/HTML/template_export.html" \
  --password "abcd-efgh-ijkl-mnop"
```

#### Astuce (Variables d'environnement) :
Vous pouvez éviter de retaper votre mot de passe à chaque fois en exportant les variables dans votre terminal :
```bash
export ICLOUD_EMAIL="votre-adresse@icloud.com"
export ICLOUD_APP_PASSWORD="abcd-efgh-ijkl-mnop"
```

---

## 🎨 Composants GitHub Inclus dans le Studio

Le Studio prend en charge l'ensemble des éléments de présentation GitHub :

### 1. Blocs d'Alertes (GitHub Flavored Callouts)
Saisissez simplement cette syntaxe dans le Markdown :
* `> [!NOTE]` : Information générale ou précision.
* `> [!TIP]` : Conseil pratique ou bonne idée.
* `> [!IMPORTANT]` : Point critique à ne pas manquer.
* `> [!WARNING]` : Avertissement ou rappel d'échéance.

### 2. Badges de Statut
Utilisez la syntaxe inline code avec des backticks :
* `` `VALIDÉ` ``
* `` `EN COURS` ``
* `` `URGENT` ``

### 3. Tableaux Comparatifs & Matrice de Données
```markdown
| Action | Responsable | Échéance | Statut |
| :--- | :--- | :--- | :--- |
| Audit RSE | Julien F. | 28/08/2026 | `VALIDÉ` |
```

### 4. Boutons d'Action (Call To Action - CTA)
```markdown
[Consulter l'Espace Projet](https://github.com)
```

---

## 🛠️ Dépannage

* **Le formatage disparaît au collage dans Apple Mail ?**  
  Vérifiez que votre message Apple Mail est configuré en mode **Texte Enrichi** (`Format > Format Texte Enrichi` ou `Cmd + Shift + T`).
* **Erreur `SMTPAuthenticationError` lors de l'exécution du script Python ?**  
  Assurez-vous d'utiliser un mot de passe spécifique d'application Apple (4 groupes de 4 caractères séparés par des tirets) et non le mot de passe de votre compte iCloud général.
