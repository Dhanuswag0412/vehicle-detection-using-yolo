from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

vehicle_classes = ["car", "bus", "truck", "motorcycle", "bicycle"]

def detect_vehicles(image_path):
    
    results = model(image_path)

    
    annotated_image = results[0].plot()

    
    vehicle_count = 0

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        label = model.names[class_id]

        if label in vehicle_classes:
            vehicle_count += 1

    return annotated_image, vehicle_count