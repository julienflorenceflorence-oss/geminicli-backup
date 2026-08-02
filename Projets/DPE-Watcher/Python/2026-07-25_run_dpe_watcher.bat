@echo off
:: run_dpe_watcher.bat
:: Ce script bat est conçu pour lancer l'exécution quotidienne du DPE Watcher
:: Il peut être associé directement au Planificateur de tâches Windows (Task Scheduler).

echo ===================================================
echo Lancement du DPE Watcher - %date% %time%
echo ===================================================

:: Positionnement dans le dossier du script Python
cd /d "%~dp0"

:: Verification de la presence de l'executable binaire compile (.exe)
if exist "dpe_watcher.exe" (
    echo Lancement de l'executable dpe_watcher.exe...
    dpe_watcher.exe
) else (
    echo Executable introuvable. Tentative avec le script Python...
    if exist ".venv\Scripts\activate.bat" (
        echo Activation de l'environnement virtuel local .venv...
        call ".venv\Scripts\activate.bat"
    )
    python dpe_watcher.py
)

echo ===================================================
echo Execution terminee.
echo ===================================================
