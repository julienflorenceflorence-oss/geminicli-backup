import os
import asyncio
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Erreur : La bibliothèque 'playwright' n'est pas installée.")
    sys.exit(1)

async def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "carte.html"))
    output_dir = os.path.normpath(os.path.join(base_path, "..", "..", "04_Livrables", "Images"))
    output_path = os.path.join(output_dir, "Carte_Julien_Florence_Capitole.png")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("[*] Lancement du navigateur pour capturer la carte...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Définir un appareil mobile ou un viewport adapté
        context = await browser.new_context(
            viewport={'width': 480, 'height': 800},
            device_scale_factor=2 # Haute résolution pour impression / partage
        )
        page = await context.new_page()

        try:
            await page.goto(f"file://{html_path}", wait_until="networkidle")
            # Attente de chargement des images
            await page.wait_for_timeout(2000)

            # Cibler le conteneur de la carte de visite
            card = await page.query_selector(".card-container")
            if card:
                print("[*] Capture de la carte de visite (.card-container) en haute résolution...")
                await card.screenshot(
                    path=output_path,
                    omit_background=True # Transparence autour des coins arrondis
                )
                print(f"[OK] Carte générée avec succès en PNG transparent : {output_path}")
            else:
                print("[X] Erreur : L'élément '.card-container' est introuvable.")
        except Exception as e:
            print(f"[X] Une erreur est survenue : {str(e)}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
