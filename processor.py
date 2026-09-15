import cv2
import numpy as np
from yoloface import face_analysis

face_detector = face_analysis()

def blur_face(face, factor=3.0):
    h, w = face.shape[:2]
    kW = max(3, int(w / factor))
    kH = max(3, int(h / factor))
    kW += (kW % 2 == 0)
    kH += (kH % 2 == 0)
    return cv2.GaussianBlur(face, (kW, kH), 0)

def pixelate_face(face, blocks=12):
    h, w = face.shape[:2]
    x_steps = np.linspace(0, w, blocks + 1, dtype=int)
    y_steps = np.linspace(0, h, blocks + 1, dtype=int)
    for i in range(1, len(y_steps)):
        for j in range(1, len(x_steps)):
            x1, y1 = x_steps[j - 1], y_steps[i - 1]
            x2, y2 = x_steps[j], y_steps[i]
            roi = face[y1:y2, x1:x2]
            if roi.size == 0:
                continue
            color = cv2.mean(roi)[:3]
            cv2.rectangle(face, (x1, y1), (x2, y2), color, -1)
    return face

def process_image(image_path, method="blur"):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not load image")

    _, boxes, _ = face_detector.face_detection(image_path, model='tiny')

    if boxes is None or len(boxes) == 0:
        print("No faces detected")
        return image

    print(f"Detected {len(boxes)} faces")

    for box in boxes:
        x, y, h, w = box

        expand = 0.4
        x1 = max(0, int(x - w * expand))
        y1 = max(0, int(y - h * expand))
        x2 = min(image.shape[1], int(x + w * (1 + expand)))
        y2 = min(image.shape[0], int(y + h * (1 + expand)))

        face_roi = image[y1:y2, x1:x2]
        if face_roi.size == 0:
            continue

        if method == "blur":
            processed = blur_face(face_roi)
        else:
            processed = pixelate_face(face_roi)

        image[y1:y2, x1:x2] = processed

    return image