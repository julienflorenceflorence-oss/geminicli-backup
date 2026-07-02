@echo off
:: run_dpe_watcher.bat
:: Ce script bat est conçu pour lancer l'exécution quotidienne du DPE Watcher
:: Il peut être associé directement au Planificateur de tâches Windows (Task Scheduler).

echo ===================================================
echo Lancement du DPE Watcher - %date% %time%
echo ===================================================

:: Positionnement dans le dossier du script Python
cd /d "%~dp0"

:: Verification de la presence de l'environnement virtuel (.venv)
if exist ".venv\Scripts\activate.bat" (
    echo Activation de l'environnement virtuel local .venv...
    call ".venv\Scripts\activate.bat"
) else (
    echo Aucun environnement virtuel .venv trouve. Utilisation du Python global.
)

:: Execution du script Python
python dpe_watcher.py

echo ===================================================
echo Execution terminee.
echo ===================================================
