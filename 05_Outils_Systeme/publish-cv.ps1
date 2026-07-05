# publish-cv.ps1
# Script de publication propre du CV Interactif vers cv-prestige.git (excluant les fichiers privés)

$SourcePath = "C:\Users\julien\OneDrive\Bureau\geminicli\Projets\prospection job\chef-ventes-michaelpage"
$TempPath = Join-Path -Path $env:TEMP -ChildPath "cv-prestige-publish"
$PublicRemote = "https://github.com/julienflorenceflorence-oss/cv-prestige.git"

Write-Output "=== DEBUT DE LA PUBLICATION DU CV INTERACTIF ==="

# 1. Nettoyer le dossier temporaire
if (Test-Path -Path $TempPath) {
    Remove-Item -Path $TempPath -Recurse -Force
}
$null = New-Item -Path $TempPath -ItemType Directory -Force

# 2. Copier uniquement les fichiers nécessaires
Write-Output "Copie des fichiers publics..."
$FilesToCopy = @(
    "index.html",
    "diplomes.html",
    "bachelor-status.html",
    "viewer.html"
)

$FoldersToCopy = @(
    "photo",
    "video",
    "diplomes cadre",
    "PDF"
)

foreach ($file in $FilesToCopy) {
    $src = Join-Path $SourcePath $file
    if (Test-Path -Path $src) {
        Copy-Item -Path $src -Destination $TempPath -Force
    }
}

foreach ($folder in $FoldersToCopy) {
    $src = Join-Path $SourcePath $folder
    $dest = Join-Path $TempPath $folder
    if (Test-Path -Path $src) {
        Copy-Item -Path $src -Destination $dest -Recurse -Force
    }
}

# 3. Initialiser le dépôt propre dans le dossier temporaire
Set-Location -Path $TempPath
git init -b main
git remote add origin $PublicRemote

# Configurer l'utilisateur pour le dépôt public
git config user.name "Julien Florence"
git config user.email "julienflorenceflorence@gmail.com"

# Ajouter et commiter
git add -A
git commit -m "Deploy interactive CV (Clean build)"

# 4. Pousser de force sur le dépôt public GitHub Pages
Write-Output "Mise à jour forcée du dépôt public cv-prestige..."
git push --force origin main 2>&1

# 5. Retourner au dossier d'origine
Set-Location -Path "C:\Users\julien\OneDrive\Bureau\geminicli"
Remove-Item -Path $TempPath -Recurse -Force

Write-Output "=== DEPLOYEMENT DU CV INTERACTIF REUSSI ET CLARIFIE ==="
