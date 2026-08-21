#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=============================================================================
iCloud Mail SMTP Sender — Script Python d'Envoi d'Emails HTML
=============================================================================
Permet d'envoyer des e-mails HTML enrichis (rendus par l'iCloud Email Studio)
directement depuis votre compte de messagerie iCloud (@icloud.com / @me.com).

Exemple d'utilisation :
  python3 send_icloud_email.py \
    --from "votre-adresse@icloud.com" \
    --to "destinataire@exemple.com" \
    --subject "🚀 Compte-Rendu Stratégique" \
    --html-file "../HTML/template_export.html" \
    --password "abcd-efgh-ijkl-mnop"
=============================================================================
"""

import argparse
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

ICLOUD_SMTP_SERVER = "smtp.mail.me.com"
ICLOUD_SMTP_PORT = 587


def send_icloud_email(sender, recipient, subject, html_content, password, attachment_path=None):
    """Envoie un e-mail au format HTML via les serveurs SMTP iCloud."""
    
    print("==================================================")
    print("🚀 iCloud Mail SMTP Sender — Initialisation")
    print("==================================================")
    print(f"📧 Expéditeur   : {sender}")
    print(f"📬 Destinataire : {recipient}")
    print(f"📌 Objet        : {subject}")
    print(f"🌐 Serveur SMTP : {ICLOUD_SMTP_SERVER}:{ICLOUD_SMTP_PORT} (STARTTLS)")
    print("--------------------------------------------------")

    # Construction du message MIME
    msg = MIMEMultipart('alternative')
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Version texte brut fallback pour les clients très anciens
    text_fallback = "Veuillez activer l'affichage HTML dans votre client de messagerie pour visualiser cet e-mail enrichi."
    part_text = MIMEText(text_fallback, 'plain', 'utf-8')
    part_html = MIMEText(html_content, 'html', 'utf-8')

    msg.attach(part_text)
    msg.attach(part_html)

    # Ajout d'une pièce jointe éventuelle
    if attachment_path:
        if os.path.exists(attachment_path):
            print(f"📎 Ajout de la pièce jointe : {attachment_path}")
            with open(attachment_path, "rb") as f:
                part_attach = MIMEBase("application", "octet-stream")
                part_attach.set_payload(f.read())
            encoders.encode_base64(part_attach)
            filename = os.path.basename(attachment_path)
            part_attach.add_header("Content-Disposition", f'attachment; filename="{filename}"')
            msg.attach(part_attach)
        else:
            print(f"⚠️ Pièce jointe introuvable : {attachment_path}")

    # Connexion SMTP avec TLS
    try:
        print("🔒 Connexion et sécurisation TLS en cours...")
        server = smtplib.SMTP(ICLOUD_SMTP_SERVER, ICLOUD_SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()

        print("🔑 Authentification avec le mot de passe d'application Apple...")
        server.login(sender, password)

        print("✉️ Envoi de l'e-mail en cours...")
        server.sendmail(sender, [recipient], msg.as_string())
        server.quit()

        print("==================================================")
        print("✅ E-mail envoyé avec succès via iCloud Mail !")
        print("==================================================")
        return True

    except smtplib.SMTPAuthenticationError:
        print("\n❌ ÉCHEC D'AUTHENTIFICATION !")
        print("👉 Assurez-vous d'utiliser un Mot de Passe Spécifique à une Application généré sur https://appleid.apple.com")
        print("   (et NON le mot de passe principal de votre compte Apple).")
        return False
    except Exception as e:
        print(f"\n❌ ERREUR LORS DE L'ENVOI : {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Envoi d'e-mails HTML via la messagerie iCloud.")
    parser.add_argument("--from", dest="sender", help="Votre adresse e-mail iCloud (@icloud.com / @me.com)")
    parser.add_argument("--to", dest="recipient", required=True, help="Adresse e-mail du destinataire")
    parser.add_argument("--subject", required=True, help="Sujet de l'e-mail")
    parser.add_argument("--html-file", help="Chemin vers le fichier HTML généré par le Studio")
    parser.add_argument("--html", help="Contenu HTML direct sous forme de chaîne de caractères")
    parser.add_argument("--password", help="Mot de passe d'application Apple ID")
    parser.add_argument("--attach", help="Chemin vers une pièce jointe (optionnel)")

    args = parser.parse_args()

    # Si l'expéditeur n'est pas fourni, demander ou utiliser la variable d'environnement
    sender = args.sender or os.environ.get("ICLOUD_EMAIL")
    if not sender:
        sender = input("Saisissez votre adresse iCloud (@icloud.com) : ").strip()

    # Si le mot de passe n'est pas fourni, demander ou utiliser la variable d'environnement
    password = args.password or os.environ.get("ICLOUD_APP_PASSWORD")
    if not password:
        import getpass
        password = getpass.getpass("Saisissez votre mot de passe d'application Apple ID : ").strip()

    # Lecture du contenu HTML
    html_content = ""
    if args.html_file:
        if os.path.exists(args.html_file):
            with open(args.html_file, "r", encoding="utf-8") as f:
                html_content = f.read()
        else:
            print(f"❌ Erreur : Fichier HTML introuvable ({args.html_file})")
            sys.exit(1)
    elif args.html:
        html_content = args.html
    else:
        print("❌ Erreur : Veuillez spécifier un fichier HTML (--html-file) ou du contenu HTML (--html)")
        sys.exit(1)

    success = send_icloud_email(sender, args.recipient, args.subject, html_content, password, args.attach)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
