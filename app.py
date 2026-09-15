from flask import Flask, render_template, request, send_from_directory
import os
import uuid
from processor import process_image
import cv2

app = Flask(__name__, template_folder="templates")

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    original_image = None
    processed_image = None

    if request.method == "POST":
        file = request.files.get("image")
        method = request.form.get("method", "blur")

        if file and file.filename != "":
            # Keep original extension so browser displays the uploaded photo correctly
            ext = os.path.splitext(file.filename)[1].lower() or ".png"
            unique_id = str(uuid.uuid4())
            input_path = os.path.join(UPLOAD_FOLDER, unique_id + ext)
            output_path = os.path.join(OUTPUT_FOLDER, unique_id + ".png")  # we always save output as PNG

            file.save(input_path)

            # Process with your YOLOFace pipeline
            result = process_image(input_path, method=method)
            cv2.imwrite(output_path, result)

            # Paths for the template
            original_image = f"uploads/{unique_id}{ext}"
            processed_image = f"outputs/{unique_id}.png"

    return render_template(
        "index.html",
        original_image=original_image,
        processed_image=processed_image
    )

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/outputs/<filename>")
def output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)