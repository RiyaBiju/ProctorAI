from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")

# Run detection on video
model.predict(
    source="video.mp4",
    show=True,
    save=True,
    conf=0.5
)