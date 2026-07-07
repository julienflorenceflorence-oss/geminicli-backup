import os
import imageio
from PIL import Image
import numpy as np

def convert_mp4_to_gif():
    base_path = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "video", "cerveau41.mp4"))
    dest_path = os.path.normpath(os.path.join(base_path, "..", "HTML", "video", "cerveau_42.gif"))

    if not os.path.exists(source_path):
        print(f"[X] Source introuvable : {source_path}")
        return

    print(f"[*] Lecture de la vidéo MP4 : {source_path}...")
    reader = imageio.get_reader(source_path)
    
    print("[*] Optimisation ultime (1 frame sur 4, largeur 400px, vitesse originale 24 FPS)...")
    # Nous lisons 1 frame sur 4 (pour diviser par 4 le poids initial)
    # et écrivons le GIF à 6 FPS (24 / 4 = 6) pour conserver exactement la même vitesse d'exécution
    writer = imageio.get_writer(dest_path, fps=6.0, loop=0)
    
    count = 0
    for frame in reader:
        if count % 4 == 0:
            # Redimensionner à 400px de large (excellent compromis qualité/poids pour e-mail)
            img = Image.fromarray(frame)
            img.thumbnail((400, 400))
            writer.append_data(np.array(img))
        count += 1
        
    writer.close()
    print(f"[OK] GIF animé ultra-optimisé généré : {dest_path}")

if __name__ == "__main__":
    convert_mp4_to_gif()
