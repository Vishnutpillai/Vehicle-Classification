![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-AI-orange)
![CNN](https://img.shields.io/badge/CNN-Convolutional%20Neural%20Network-green)
![MobileNetV2](https://img.shields.io/badge/MobileNetV2-Transfer%20Learning-red)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Keras](https://img.shields.io/badge/Keras-Neural%20Network-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Deployment-black)
![HTML](https://img.shields.io/badge/HTML-Web-orange)
![CSS](https://img.shields.io/badge/CSS-Styling-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 🚗 Vehicle Image Classification Using Deep Learning and Transfer Learning

## 📌 Project Overview

Vehicle Image Classification is a Computer Vision based Deep Learning project that automatically identifies different types of vehicles from images.

The project uses **Convolutional Neural Network (CNN)** concepts and **Transfer Learning with MobileNetV2** to achieve efficient and accurate image classification.

The complete pipeline includes:

* Data preprocessing
* Image augmentation
* CNN-based feature extraction
* MobileNetV2 transfer learning
* Model evaluation
* Flask deployment

---

# 🎯 Project Objective

The main objective of this project is to develop an AI-powered vehicle classification system that can recognize vehicle categories from images.

The system helps in:

* Automated vehicle identification
* Computer vision applications
* Smart transportation systems
* AI-based image analysis

---

# 🧠 Technologies Used

## Programming Language

* Python

## Deep Learning

* TensorFlow
* Keras
* MobileNetV2
* CNN

## Computer Vision

* OpenCV
* NumPy

## Data Analysis

* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

# 🚘 Vehicle Classes

The model classifies images into:

* Bicycle
* Bus
* Car
* Ship
* Train
* Truck
* Aeroplane
* Motorcycle

---

# 🏗️ Model Architecture

## MobileNetV2 Transfer Learning

MobileNetV2 is a lightweight CNN architecture designed for image classification.

Advantages:

* Faster training
* Lower computational cost
* High accuracy
* Suitable for deployment

Architecture:

```
Input Image
     |
     ↓
Image Preprocessing
     |
     ↓
MobileNetV2 Feature Extraction
     |
     ↓
Global Average Pooling
     |
     ↓
Dense Layer
     |
     ↓
Softmax Classification
```

---

# 👁️ Computer Vision Pipeline

```
Image Input

      ↓

OpenCV Processing

      ↓

Resize Image (224 × 224)

      ↓

Normalize Pixel Values

      ↓

MobileNetV2 Prediction

      ↓

Vehicle Class + Confidence Score
```

---

# 🔥 Training Process

The notebook includes:

* Dataset loading
* Data preprocessing
* Data augmentation
* Train validation split
* MobileNetV2 model creation
* Model training
* Performance evaluation

Callbacks used:

## EarlyStopping

Stops training when validation performance stops improving.

## ModelCheckpoint

Automatically saves the best performing model.

Saved model:

```
best_vehicle_model.h5
```

---

# 📊 Model Output

Example:

```
Prediction:

Vehicle: Car

Confidence: 96.8%
```

---

# 📂 Project Structure

```
Vehicle Classification Project

│
├── Dataset
│
├── Vehicle Classification.ipynb
│
├── requirements_training.txt
│
└── vehicle_app
    │
    ├── app.py
    ├── best_vehicle_model.h5
    ├── requirements.txt
    │
    ├── static
    │
    └── templates
```

---

# 🚀 Future Improvements

* Real-time vehicle detection
* YOLO object detection integration
* Mobile application deployment
* Larger vehicle dataset
* Cloud based AI deployment

---

# 👨‍💻 Author

Deep Learning Computer Vision Project
