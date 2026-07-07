import os
import imageio
from PIL import Image
import numpy as np

def convert_mp4_to_gif():
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Utiliser la vidéo haute qualité de 210 frames à 24 FPS
    source_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "video", "cerveau41.mp4"))
    dest_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "video", "cerveau_42.gif"))

    if not os.path.exists(source_path):
        print(f"[X] Source introuvable : {source_path}")
        return

    print(f"[*] Lecture de la vidéo MP4 : {source_path}...")
    reader = imageio.get_reader(source_path)
    
    print("[*] Optimisation et conversion en GIF animé (vitesse originale 24 FPS)...")
    # Nous lisons 1 frame sur 2 (pour diviser par 2 le nombre de frames) 
    # et écrivons le GIF à 12 FPS pour conserver exactement la même vitesse d'exécution
    writer = imageio.get_writer(dest_path, fps=12.0, loop=0)
    
    count = 0
    for frame in reader:
        if count % 2 == 0:
            # Redimensionner le frame à 500px de large pour optimiser le poids e-mail
            img = Image.fromarray(frame)
            img.thumbnail((500, 500))
            # Convertir en tableau numpy pour imageio
            writer.append_data(np.array(img))
        count += 1
        
    writer.close()
    print(f"[OK] GIF animé haute vitesse et optimisé généré : {dest_path}")

if __name__ == "__main__":
    convert_mp4_to_gif()
