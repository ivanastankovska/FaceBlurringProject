# Face Blurring Application

A web application for automatic face detection and anonymization in uploaded images. Built with Flask and OpenCV, it uses YOLO-based face detection to locate faces and applies Gaussian blur or pixelation to protect privacy.

## Features

- **Multi-face detection** — Uses YOLOFace to detect and process multiple faces in a single image
- **Privacy protection** — Applies Gaussian blur and pixelation techniques via OpenCV to anonymize detected faces
- **Web-based interface** — Simple, clean UI for uploading images, previewing results, and downloading processed output
- **Flask backend** — Handles image upload, processing pipeline, and result delivery

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Face Detection | YOLOFace |
| Image Processing | OpenCV |
| Frontend | HTML, CSS |

## How It Works

1. User uploads an image through the web interface
2. The image is passed to the YOLOFace detection model, which identifies face bounding boxes
3. Each detected face region is anonymized using Gaussian blur or pixelation
4. The processed image is returned to the user for preview and download

## Project Structure

```
FaceBlurringProject/
├── app.py                  # Flask application entry point
├── processor.py            # Image processing and face detection logic
├── templates/
│   └── index.html          # Web interface
├── models/
│   └── deploy.prototxt     # Model configuration
├── .yoloface/
│   ├── face_detection.cfg
│   ├── face_detection.weights      # YOLO weights (not included — see setup)
│   ├── yolov3_tiny_face.cfg
│   └── yolov3-tiny_face.weights    # YOLO weights (not included — see setup)
├── uploads/                # User-uploaded images (runtime, gitignored)
├── outputs/                # Processed images (runtime, gitignored)
└── requirements.txt
```

## Setup

### Prerequisites

- Python 3.9+
- pip

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/ivanastankovska/FaceBlurringProject.git
   cd FaceBlurringProject
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. **Download the YOLOFace model weights.** These files are too large for GitHub and are not included in this repository. Download them from the official source and place them in the `.yoloface/` directory:
   - `face_detection.weights`
   - `yolov3-tiny_face.weights`

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser to `http://localhost:5000`

## Usage

1. Open the web app in your browser
2. Upload an image containing one or more faces
3. The app detects all faces and applies blurring/pixelation automatically
4. Preview the processed result and download it

## Notes

- Processing is done entirely server-side; no images are stored beyond the current session's `uploads/` and `outputs/` folders.
- Detection accuracy depends on the YOLOFace model's confidence threshold, which can be tuned in `processor.py`.

## License

This project is for educational purposes.
