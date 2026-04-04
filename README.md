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

best.pt              # Trained YOLOv8 model weights
├── detect_webcam.py     # Real-time detection via webcam
├── test_video.py        # Detection on recorded video files
├── code (1).ipynb       # Training and experimentation notebook
├── results.csv          # Model output: classes, confidence scores, statistics
├── requirements.txt     # Python dependencies
└── README.md

Setup
Requirements: Python 3.8+
bashpip install -r requirements.txt
Key dependencies include PyTorch, OpenCV, and Ultralytics YOLO.

Usage
Live webcam detection
bashpython detect_webcam.py
Run on a recorded video
bashpython test_video.py --source path/to/video.mp4

Model

Architecture: YOLOv8 nano (yolov8n) fine-tuned at 640px input
Classes: helmet, no-helmet, vest, no-vest, worker
Tracker: ByteTrack for consistent per-worker IDs across frames
Dataset source: Roboflow Universe — PPE Detection dataset


How It Works

Each video frame is passed to the YOLOv8 model for object detection
Detections are handed to ByteTrack, which assigns and maintains a unique ID per worker across frames
Bounding boxes and labels are drawn on the frame with color coding by class
Per-frame counts are computed for each class (workers present, helmets detected, violations, etc.)
Annotated frames are written to the output stream or saved to disk


Outputs
OutputDescriptionAnnotated videoFrames with bounding boxes and class labels overlaidPer-frame countsNumber of workers, PPE items detected, and violationsTracked predictionsRaw JSON with track IDs, class names, confidence scores

Extending the System
Alerts — Add a condition check for no-helmet or no-vest detections and route to a Slack or email notification.
Logging — Pipe the raw predictions (track IDs, class names, confidence scores, timestamps) to a database or dashboard for compliance reporting and audit trails.
Retraining — Validate the model on your own site footage. Use active learning by uploading new annotated frames to Roboflow and retraining periodically to improve accuracy for your environment.

License
This project is for educational and research use
