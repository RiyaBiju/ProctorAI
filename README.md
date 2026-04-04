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


This workflow detects Personal Protective Equipment (PPE) — such as helmets and safety vests — on construction workers in real-time webcam feeds or recorded video clips. It tracks detected workers and gear across frames to ensure consistent safety monitoring and produces annotated video output for safety oversight.

Approach
A fine-tuned YOLOv8 nano object detection model identifies workers and their PPE (helmets, vests, etc.) in each frame. Detected objects are passed to a ByteTrack tracker to maintain consistent IDs across frames — critical for monitoring compliance over time. Bounding boxes and labels are rendered on each frame, and a running count of detected PPE items is computed per frame.

Models
PPE Detection Model: yolov8n-640 (YOLOv8 nano) fine-tuned for construction PPE classes such as helmet, vest, worker, no-helmet, no-vest. Train or source a dataset from Roboflow Universe (e.g., roboflow-100/ppe-detection).
Workflow Steps
Input: Accept an image (frame from webcam or video clip — the platform handles frame extraction automatically).

Detect PPE and workers: Run the YOLOv8 nano PPE detection model on the incoming frame to identify workers and their safety equipment (helmets, vests, and violations like missing gear). [Object Detection Model]

Track detections across frames: Pass the detections to ByteTrack to assign and maintain consistent object IDs across video frames, enabling per-worker tracking over time. [Byte Tracker]

Visualize bounding boxes: Draw color-coded bounding boxes around each tracked detection (workers, helmets, vests, violations) on the frame. [Bounding Box Visualization]

Overlay labels: Render class name (e.g., "Helmet", "No Vest") and confidence score labels on each bounding box, positioned above each detection for readability. [Label Visualization]

Count detections per class: Compute the total number of detections per frame (e.g., number of workers, helmets present, violations detected) using a property definition. [Property Definition]

Outputs:

Annotated video frame with bounding boxes and class labels.
Per-frame detection count (total workers, PPE items, violations).
Raw tracked predictions (with track IDs) for downstream processing.
Beyond the Workflow
Alerting: If you want to trigger alerts when a worker is detected without a helmet or vest, add an [Expression] block to check if any detection has class no-helmet or no-vest, and route to a [Slack Notification] or [Email Notification] block.
Logging: Pipe the raw predictions JSON (including track IDs, class names, confidence scores, and timestamps) to a database or dashboard system outside the workflow for compliance reporting and audit trails.
Model training: If using a pre-built model from Roboflow Universe, validate it on your site-specific footage and retrain via active learning using [Roboflow Dataset Upload] to continuously improve accuracy.
