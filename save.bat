@echo off
rem Script de sauvegarde ultra-rapide 1-clic pour Windows PC

set MSG=%~1
if "%MSG%"=="" set MSG=Sauvegarde automatique PC - %date% %time%

echo 🔄 Sauvegarde en cours sur GitHub...
git add .
git commit -m "%MSG%"
git push origin main
echo ✅ Synchronisation GitHub terminée !
