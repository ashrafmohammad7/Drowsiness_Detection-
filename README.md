# 💤 Drowsiness Detection System

A Deep Learning based web application that detects whether a person is drowsy or non-drowsy using eye images.

## 🚀 Live Deployment
https://drowsiness-detection-d8x1.onrender.com

---

## 📌 Features
- Upload eye image
- Detect drowsy/non-drowsy state
- Deep Learning model using TensorFlow/Keras
- Flask web application
- Real-time prediction confidence
- Responsive web interface

---

## 🛠️ Technologies Used
- Python
- Flask
- TensorFlow / Keras
- OpenCV
- NumPy
- HTML/CSS

---

## 📂 Project Structure

```bash
Drowsiness_Detection/
│
├── app.py
├── train.py
├── prepare_dataset.py
├── eye_model.h5
├── requirements.txt
├── runtime.txt
├── Procfile
├── render.yaml
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
```

---

## ⚙️ Installation

```bash
git clone https://github.com/ashrafmohammad7/Drowsiness_Detection-.git
cd Drowsiness_Detection-
pip install -r requirements.txt
python app.py
```

---

## 🧠 Model Training

```bash
python train.py
```

---

## 🌐 Deployment

Deployed using Render.