# 🚗 Vehicle Classification Flask Web Application

## 📌 Overview

This folder contains the Flask deployment application for the trained Vehicle Classification Deep Learning model.

The application loads the trained **MobileNetV2 model** and provides a web interface where users can upload vehicle images and get prediction results.

---

# ✨ Features

* Image upload system
* Deep Learning prediction
* MobileNetV2 model integration
* OpenCV preprocessing
* Confidence score calculation
* Non-vehicle image detection
* Professional web interface

---

# 🏗️ Application Workflow

```
User Upload Image

        ↓

Flask Application

        ↓

OpenCV Image Processing

        ↓

MobileNetV2 Model

        ↓

Prediction

        ↓

Confidence Result Display
```

---

# 🛠️ Technologies Used

* Python
* Flask
* TensorFlow
* Keras
* MobileNetV2
* OpenCV
* HTML
* CSS

---

# 📂 Folder Structure

```
vehicle_app

│
├── app.py
│
├── best_vehicle_model.h5
│
├── requirements.txt
│
├── static
│    │
│    ├── style.css
│    │
│    └── uploads
│
└── templates
     │
     ├── home.html
     │
     └── prediction.html
```

---

# ⚙️ Installation

Create environment:

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶️ Run Application

Start Flask:

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 📦 Requirements

```
Flask
tensorflow
numpy
opencv-python-headless
gunicorn
```

---

# ☁️ Deployment

Supported platforms:

* Render
* AWS EC2
* Hugging Face Spaces
* Railway

Production command:

```
gunicorn app:app
```

---

# 🔐 Prediction Logic

The application checks confidence:

Example:

```
Confidence > 70%

→ Vehicle class

Confidence < 70%

→ Non Vehicle
```

---

# 🔮 Future Improvements

* Live camera prediction
* API endpoint creation
* Docker deployment
* Cloud GPU inference

---

# 👨‍💻 Author

Vehicle Classification AI Deployment Project
