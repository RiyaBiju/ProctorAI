# Hard Hat Safety Detection using YOLOv8

## Overview
This project implements a real-time helmet safety detection system using the YOLOv8 object detection framework. The model is trained to detect different helmet safety conditions and can run on images, videos, and live webcam feeds.

The system aims to assist in ppe detection by identifying workers are not wearing helmets or wearing helmets improperly.

---

## Features
- Real-time helmet detection
- Detection on images
- Detection on video files
- Live webcam detection
- CSV logging of detection results
- Custom-trained YOLOv8 model

---

## Technologies Used
- Python
- Ultralytics YOLOv8
- OpenCV
- NumPy

---

📄 README.md

Contains the project overview, objectives, setup instructions, and usage guide for the PPE detection system.

🤖 best.pt

The trained YOLO model weights used for detecting Personal Protective Equipment (PPE) such as helmets.

📓 code (1).ipynb

A Jupyter Notebook used during development for:

Training the YOLO model

Testing detection results

Experimenting with parameters and dataset

📷 detect_webcam.py

Python script for real-time PPE detection using a webcam.

Functions:

Captures live webcam frames

Runs YOLO object detection

Displays bounding boxes for detected PPE

📦 requirements.txt

Contains the list of required Python libraries needed to run the project.

Example dependencies may include:

PyTorch

OpenCV

Ultralytics YOLO

📊 results.csv

Stores model output results such as:

Predicted classes

Confidence scores

Detection statistics

🎥 test_video.py

Script used to run PPE detection on recorded video files instead of live webcam input
