import os
import asyncio
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Erreur : La bibliothèque 'playwright' n'est pas installée.")
    print("Veuillez exécuter : pip install playwright && playwright install chromium")
    sys.exit(1)

async def generate_pdf(html_rel_path, pdf_rel_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.normpath(os.path.join(base_path, html_rel_path))
    pdf_path = os.path.normpath(os.path.join(base_path, pdf_rel_path))

    pdf_dir = os.path.dirname(pdf_path)
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    if not os.path.exists(html_path):
        print(f"[X] Erreur : Le fichier source {html_path} est introuvable.")
        return False

    print(f"[*] Traitement de {os.path.basename(html_path)}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        try:
            await page.goto(f"file://{html_path}", wait_until="networkidle")
            await page.wait_for_timeout(2000) 
            
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
            print(f"[X] Une erreur est survenue lors de la génération de {os.path.basename(html_path)} : {str(e)}")
            return False
        finally:
            await browser.close()

async def main():
    print("--- COMPILATEUR PDF EMINEO ---")
    cv_success = await generate_pdf("../HTML/CV_Julien_Florence.html", "../PDF/CV_Julien_Florence_Emineo.pdf")
    lm_success = await generate_pdf("../HTML/LM_Julien_Florence.html", "../PDF/LM_Julien_Florence_Emineo.pdf")
    arg_success = await generate_pdf("../HTML/Argumentaire_Vente.html", "../PDF/Argumentaire_Vente_Emineo.pdf")
    
    if cv_success and lm_success and arg_success:
        print("[*] Compilation de la candidature EMINEO terminée avec succès.")
    else:
        print("[X] Échec partiel ou total de la compilation.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nArrêt par l'utilisateur.")
