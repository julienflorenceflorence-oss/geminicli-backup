# publish-capitole.ps1
# Script de publication du CV Interactif Grand Hôtel Capitole vers cv-prestige.git

$ProjPath = "C:\Users\julien\OneDrive\Bureau\geminicli\Projets\prospection job\grand-hotel-capitole"
$HTMLSource = Join-Path $ProjPath "03_Travail\HTML"
$PDFSource = Join-Path $ProjPath "04_Livrables\PDF"
$TempPath = Join-Path -Path $env:TEMP -ChildPath "cv-capitole-publish"
$PublicRemote = "https://github.com/julienflorenceflorence-oss/cv-prestige.git"

Write-Output "=== DEBUT DE LA PUBLICATION DU CV GRAND HOTEL CAPITOLE ==="

# 1. Nettoyer le dossier temporaire
if (Test-Path -Path $TempPath) {
    Remove-Item -Path $TempPath -Recurse -Force
}
$null = New-Item -Path $TempPath -ItemType Directory -Force

# 2. Copier les fichiers HTML et dossiers d'accompagnement
Write-Output "Copie des fichiers HTML et médias..."
$FilesToCopy = @(
    "index.html",
    "diplomes.html",
    "bachelor-status.html",
    "viewer.html",
    "carte.html",
    "qr-code.png",
    "Carte_Julien_Florence_Capitole.png",
    "signature.html",
    "cerveau 3.0.png"
)

$FoldersToCopy = @(
    "photo",
    "video",
    "diplomes cadre",
    "histoire Happy House"
)

foreach ($file in $FilesToCopy) {
    $src = Join-Path $HTMLSource $file
    if (Test-Path -Path $src) {
        Copy-Item -Path $src -Destination $TempPath -Force
    }
}

foreach ($folder in $FoldersToCopy) {
    $src = Join-Path $HTMLSource $folder
    $dest = Join-Path $TempPath $folder
    if (Test-Path -Path $src) {
        Copy-Item -Path $src -Destination $dest -Recurse -Force
    }
}

# 3. Créer le dossier PDF et y copier les livrables PDF finaux
$TempPDFPath = Join-Path $TempPath "PDF"
$null = New-Item -Path $TempPDFPath -ItemType Directory -Force
Write-Output "Copie des PDF finaux..."
Copy-Item -Path "$PDFSource\*" -Destination $TempPDFPath -Force

# 4. Initialiser le dépôt propre dans le dossier temporaire
Set-Location -Path $TempPath
git init -b main
git remote add origin $PublicRemote

# Configurer l'utilisateur pour le dépôt public
git config user.name "Julien Florence"
git config user.email "julienflorenceflorence@gmail.com"

# Ajouter et commiter
git add -A
git commit -m "Deploy Grand Hotel Capitole interactive CV (Prestige build)"

# 5. Pousser de force sur le dépôt public GitHub Pages
Write-Output "Mise à jour forcée du dépôt public cv-prestige..."
git push --force origin main 2>&1

# 6. Retourner au dossier d'origine
Set-Location -Path "C:\Users\julien\OneDrive\Bureau\geminicli"
Remove-Item -Path $TempPath -Recurse -Force

Write-Output "=== DEPLOIEMENT DU CV CAPITOLE REUSSI AVEC SUCCES ==="
