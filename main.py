import cv2
import os

# Chemin de la vidéo à analyser
video_path = 'data/sample_video.mp4'
output_dir = 'output/frames'

# Création du dossier de sortie s'il n'existe pas
os.makedirs(output_dir, exist_ok=True)

# Chargement de la vidéo
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"❌ Impossible d’ouvrir la vidéo : {video_path}")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps * 3)  # Une image toutes les 3 secondes

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = f"{output_dir}/frame_{saved_count:04}.jpg"
        cv2.imwrite(filename, frame)
        print(f"✅ Image sauvegardée : {filename}")
        saved_count += 1

    frame_count += 1

cap.release()
print("✅ Analyse vidéo terminée.")
