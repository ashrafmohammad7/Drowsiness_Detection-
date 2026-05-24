# 🧠 AI Drowsiness Detection System Architecture

---

# 📌 Overview

The AI Drowsiness Detection System is a Deep Learning based web application that predicts whether a driver's eye state indicates drowsiness or alertness.

The application combines:
- Frontend dashboard
- Flask backend
- CNN Deep Learning model
- OpenCV preprocessing
- Detection history tracking
- Alert notification system

---

# 🏗️ System Workflow

1. User uploads an eye image
2. Flask backend receives image
3. OpenCV preprocesses image
4. Image resized to 64x64
5. CNN model performs prediction
6. System classifies:
   - Drowsy 😴
   - Non-Drowsy 👀
7. Confidence score displayed
8. Alert system activates if drowsy
9. Detection stored in history

---

# 🧠 Deep Learning Pipeline

## Input Layer
- Eye image input

## Preprocessing
- Resize image
- Normalize pixel values
- Convert to model format

## CNN Model
- Convolution layers
- Activation layers
- Pooling layers
- Dense classification layers

## Output Layer
- Binary Classification:
  - Drowsy
  - Non-Drowsy

---

# 📊 Technologies Used

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Flask (Python)

## AI/ML
- TensorFlow
- Keras
- OpenCV
- NumPy

---

# 📂 Project Components

## app.py
Handles:
- Routing
- Prediction
- Backend logic
- History tracking

## train.py
Handles:
- CNN model training
- Dataset loading
- Model saving

## index.html
Handles:
- User interface
- Dashboard
- Detection display

## detection_history.json
Stores:
- Detection results
- Confidence scores
- Timestamps

---

# 🌐 Deployment Architecture

User Browser
↓
Flask Web Server
↓
TensorFlow CNN Model
↓
Prediction Response
↓
Dashboard Visualization

---

# 🚀 Future Architecture Enhancements

- Real-time webcam detection
- Face landmark detection
- Multi-eye tracking
- Mobile deployment
- Cloud-based prediction APIs
- IoT driver safety integration