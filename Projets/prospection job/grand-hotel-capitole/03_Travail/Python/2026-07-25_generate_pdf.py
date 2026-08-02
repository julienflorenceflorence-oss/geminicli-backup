import os
import asyncio
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Erreur : La bibliothèque 'playwright' n'est pas installée.")
    print("Veuillez exécuter : pip install playwright && playwright install chromium")
    sys.exit(1)

async def generate_pdf(html_filename, pdf_filename):
    """
    Génère un PDF à partir d'un fichier HTML local en utilisant Playwright (Chromium headless).
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.normpath(os.path.join(base_path, "..", "HTML", html_filename))
    pdf_path = os.path.normpath(os.path.join(base_path, "..", "..", "04_Livrables", "PDF", pdf_filename))

    # S'assurer que le dossier de sortie PDF existe
    pdf_dir = os.path.dirname(pdf_path)
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    if not os.path.exists(html_path):
        print(f"[X] Erreur : Le fichier source {html_path} est introuvable.")
        return False

    print(f"[*] Traitement de {html_filename}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        try:
            # Chargement du fichier HTML local
            await page.goto(f"file://{html_path}", wait_until="networkidle")
            
            # Attente de chargement des polices Google Fonts
            await page.wait_for_timeout(2000) 
            
            # Génération du PDF avec les paramètres A4
            await page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                display_header_footer=False,
                margin={
                    "top": "0mm",
                    "right": "0mm",
                    "bottom": "0mm",
                    "left": "0mm",
                },
                prefer_css_page_size=True
            )
            print(f"[OK] Succès ! PDF généré : {pdf_path}")
            return True
            
        except Exception as e:
            print(f"[X] Une erreur est survenue lors de la génération de {html_filename} : {str(e)}")
            return False
        finally:
            await browser.close()

async def main():
    print("--- COMPILATEUR PDF PRESTIGE GRAND HÔTEL CAPITOLE ---")
    
    # 1. Candidature Capitole
    cv_capitole = await generate_pdf("CV_Capitole_Prestige.html", "CV_Julien_Florence_Capitole.pdf")
    lm_capitole = await generate_pdf("LM_Capitole_Prestige.html", "LM_Julien_Florence_Capitole.pdf")
    
    # 2. Candidature Générique (Postes à Responsabilité)
    cv_generique = await generate_pdf("CV_Generique_Prestige.html", "CV_Julien_Florence_Generique.pdf")
    lm_generique = await generate_pdf("LM_Generique_Prestige.html", "LM_Julien_Florence_Generique.pdf")
    
    if cv_capitole and lm_capitole and cv_generique and lm_generique:
        print("[*] Compilation de tous les livrables PDF de prestige terminée avec succès.")
    else:
        print("[X] Échec partiel ou total de la compilation.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nArrêt par l'utilisateur.")
