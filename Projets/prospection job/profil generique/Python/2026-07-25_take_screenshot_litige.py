import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1200, 'height': 1600})
        page = await context.new_page()
        
        html_path = "C:/Users/julien/OneDrive/Bureau/geminicli/Projets/prospection job/profil generique/01_Admin/2026-07-18_Mise_en_demeure_Happy_House.html"
        screenshot_path = "C:/Users/julien/OneDrive/Bureau/geminicli/Projets/prospection job/profil generique/Images/screenshot_litige.png"
        
        print(f"Loading {html_path}...")
        await page.goto(f"file:///{html_path}", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        print(f"Saving screenshot to {screenshot_path}...")
        await page.screenshot(path=screenshot_path, full_page=True)
        print("Done!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
