from flask import Flask, render_template, request
import numpy as np
import cv2
import tensorflow as tf
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder automatically if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load trained model
model = tf.keras.models.load_model("eye_model.h5")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    image_path = None

    if request.method == "POST":

        if "image" not in request.files:
            return "No file uploaded"

        file = request.files["image"]

        if file.filename == "":
            return "No file selected"

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # Read image
            img = cv2.imread(filepath)
            img = cv2.resize(img, (64, 64))
            img = img / 255.0
            img = np.reshape(img, (1, 64, 64, 3))

            # Prediction
            prediction = model.predict(img)
            confidence = float(prediction[0][0])

            if confidence > 0.5:
                result = f"Non-Drowsy 👀 (Confidence: {confidence:.2f})"
            else:
                result = f"Drowsy 😴 (Confidence: {1-confidence:.2f})"

            image_path = filepath

    return render_template("index.html",
                           result=result,
                           image_path=image_path)


if __name__ == "__main__":
    app.run(debug=True)
