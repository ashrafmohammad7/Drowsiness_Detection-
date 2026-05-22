from flask import Flask, render_template, request
import numpy as np
import cv2
import tensorflow as tf
import os
import json
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
HISTORY_FILE = "detection_history.json"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Model
model = tf.keras.models.load_model("eye_model.h5")


# =========================
# SAVE DETECTION HISTORY
# =========================
def save_history(result, confidence, image_path):

    history = []

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r") as f:

            try:
                history = json.load(f)

            except:
                history = []

    history.append({

        "result": result,

        "confidence": confidence,

        "image": image_path,

        "time": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    })

    with open(HISTORY_FILE, "w") as f:

        json.dump(history, f, indent=4)


# =========================
# HOME ROUTE
# =========================
@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    confidence = None
    image_path = None

    history = []

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r") as f:

            try:
                history = json.load(f)

            except:
                history = []

    total = len(history)

    drowsy_count = len([
        x for x in history
        if "Drowsy" in x["result"]
    ])

    non_drowsy_count = len([
        x for x in history
        if "Non-Drowsy" in x["result"]
    ])

    # =========================
    # IMAGE PREDICTION
    # =========================
    if request.method == "POST":

        if "image" not in request.files:
            return "No file uploaded"

        file = request.files["image"]

        if file.filename == "":
            return "No file selected"

        # Clear old uploads
        for old_file in os.listdir(UPLOAD_FOLDER):

            old_path = os.path.join(
                UPLOAD_FOLDER,
                old_file
            )

            try:
                os.remove(old_path)

            except:
                pass

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        # Read image
        img = cv2.imread(filepath)

        img = cv2.resize(img, (64, 64))

        img = img / 255.0

        img = np.reshape(
            img,
            (1, 64, 64, 3)
        )

        # Prediction
        prediction = model.predict(img)

        prediction_value = float(
            prediction[0][0]
        )

        # =========================
        # FIXED LABELS
        # =========================
        if prediction_value > 0.5:

            result = "Non-Drowsy 👀"

            confidence = round(
                prediction_value * 100,
                2
            )

        else:

            result = "Drowsy 😴"

            confidence = round(
                (1 - prediction_value) * 100,
                2
            )

        save_history(
            result,
            confidence,
            filepath
        )

        image_path = filepath

    return render_template(

        "index.html",

        result=result,

        confidence=confidence,

        image_path=image_path,

        history=history[::-1][:5],

        total=total,

        drowsy_count=drowsy_count,

        non_drowsy_count=non_drowsy_count
    )


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(

        host="0.0.0.0",

        port=port,

        debug=True
    )