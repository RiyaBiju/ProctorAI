import cv2
import csv
from ultralytics import YOLO

model = YOLO("best.pt")

cap = cv2.VideoCapture(0)

file = open("results.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Frame", "Class", "Confidence"])

frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_id += 1
    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls]

            writer.writerow([frame_id, label, conf])

    annotated = results[0].plot()
    cv2.imshow("Helmet Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
file.close()
cv2.destroyAllWindows()