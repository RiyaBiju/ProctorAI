🪖 Helmet Safety Detection using YOLOv8
📌 Overview

This project implements a real-time helmet safety detection system using Ultralytics YOLO and OpenCV.
The model is trained to detect different helmet safety conditions and can run on images, videos, and live webcam feeds.

The goal of the system is to help monitor motorcycle rider safety and identify violations where riders are not wearing helmets.

🎯 Features

Detects Safe Helmet

Detects Unsafe Helmet

Detects No Helmet

Works on:

Images

Videos

Live webcam

Real-time object detection

Option to save detection results to CSV

Lightweight YOLOv8 model for fast inference

🧠 Model

The detection model is trained using YOLOv8, a modern object detection architecture known for its speed and accuracy.

Model used:

yolov8s.pt

Final trained weights:

best.pt
🗂 Dataset

The dataset was created by combining and cleaning multiple headwear-related datasets.

Classes
0 → safe_helmet
1 → unsafe_helmet
2 → no_helmet
Dataset Structure
dataset/
 ├── images/
 │    ├── train
 │    ├── val
 │    └── test
 └── labels/
      ├── train
      ├── val
      └── test

Total training images: ~5000+

⚙️ Installation

Install the required libraries:

pip install ultralytics opencv-python

Required tools:

Python

Ultralytics YOLO

OpenCV
