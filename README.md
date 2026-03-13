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

README.md

Contains the project overview, objectives, and instructions to run the PPE detection system.

Provides information about the technologies used and how the project works.

best.pt

Stores the trained YOLO model weights.

This file is used by the detection scripts to identify Personal Protective Equipment (PPE) such as helmets in images or videos.

code (1).ipynb

A Jupyter Notebook used during the development phase.

Includes code for training the YOLO model, testing predictions, and experimenting with parameters.

detect_webcam.py

Python script for real-time PPE detection using a webcam.

Captures live video frames and applies the trained YOLO model to detect safety equipment.

requirements.txt

Lists all Python libraries and dependencies required to run the project.

Helps users install necessary packages easily using pip install -r requirements.txt.

results.csv

Stores detection results and output data generated during model evaluation or testing.

May include predictions, confidence scores, and other metrics.

test_video.py

Script used to run PPE detection on pre-recorded video files.

Processes video frames and applies the trained model to detect helmets and other safety gear.
