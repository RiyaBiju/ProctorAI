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

best.pt
Trained YOLO model weights used for detecting Personal Protective Equipment (PPE) such as helmets from images or video streams.

code (1).ipynb
Jupyter Notebook used for model training, experimentation, and testing object detection results during development.

detect_webcam.py
Python script that runs the trained YOLO model on a live webcam feed to detect PPE in real-time.

requirements.txt
List of required Python libraries and dependencies needed to run the project (e.g., OpenCV, PyTorch, Ultralytics YOLO).

results.csv
Stores detection results such as predicted classes, confidence scores, and other evaluation outputs from the model.

test_video.py
Script used to test the PPE detection model on pre-recorded video files instead of a live webcam.
