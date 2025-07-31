# Helmet Analyzer

This project analyzes a video recorded in the street and automatically detects cyclists wearing helmets, the dominant color of the helmet, the type of transport (bike, scooter), and allows manual input for gender and helmet brand/model.

## 🎯 Goals
- Load a video file (.mp4, .mov)
- Detect each cyclist passing in front of the camera
- Identify if they are wearing a helmet
- Extract the helmet color
- Allow manual entry of brand/model/gender
- Export all results in CSV format

## ⚙️ Tech Stack
- Python 3.10+
- OpenCV
- YOLOv8 (via Ultralytics)
- Pillow (for color detection)
- Streamlit or Tkinter (for manual review)
- Pandas (for CSV export)

## 📂 Folder structure
helmet-analyzer/
│
├── main.py                    # Main script: load video, run detection, export results
├── video_processing.py        # Detect cyclist appearances, extract frames
├── detection.py               # Run YOLOv8 to detect helmet, bike, person
├── color_extraction.py        # Extract helmet color from bounding box
├── ui_manual_input.py         # Optional interface for entering brand/gender manually
├── export.py                  # Combine data and export to CSV
│
├── data/                      # Video files to analyze
│   └── sample_video.mp4
│
├── output/                    # Exported results
│   └── results.csv
│
├── README.md
└── requirements.txt
