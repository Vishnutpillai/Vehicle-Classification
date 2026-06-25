# 🚗 Vehicle Image Classification Using Deep Learning & MobileNetV2

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow">

<img src="https://img.shields.io/badge/CNN-Computer%20Vision-green?style=for-the-badge">

<img src="https://img.shields.io/badge/MobileNetV2-Transfer%20Learning-red?style=for-the-badge">

<img src="https://img.shields.io/badge/Streamlit-Deployment-brightgreen?style=for-the-badge&logo=streamlit">

</p>


# 📌 Project Overview

Vehicle Image Classification is a Deep Learning based Computer Vision application that automatically identifies vehicle categories from uploaded images.

This project uses **Transfer Learning with MobileNetV2 CNN architecture** to achieve efficient and accurate vehicle classification.

A professional **Streamlit web application** is developed where users can upload an image and get:

- Vehicle category prediction
- Confidence score
- Non-vehicle detection
- Prediction probability visualization


---

# 🚀 Application Features

✅ Deep Learning based image classification  
✅ MobileNetV2 Transfer Learning model  
✅ CNN feature extraction  
✅ Streamlit interactive UI  
✅ Real-time image prediction  
✅ Vehicle and Non-Vehicle detection  
✅ Confidence percentage display  
✅ Prediction probability chart  
✅ Deployment ready  


---

# 🧠 Deep Learning Architecture

The project uses **MobileNetV2**, a lightweight Convolutional Neural Network designed for high performance with fewer parameters.

## Workflow

```
Input Image

      ↓

Image Preprocessing

      ↓

MobileNetV2 Feature Extraction

      ↓

Classification Layer

      ↓

Vehicle Class Prediction

```


---

# 🚘 Supported Vehicle Classes

The model can classify:

```
1. Bicycle

2. Bus

3. Car

4. Ships

5. Trains

6. Truck

7. Aeroplane

8. Motorcycle
```


### Non Vehicle Detection

If model confidence is below 70%:

```
Prediction = Non Vehicle
```


---

# 🛠️ Technology Stack


## Programming

- Python


## Deep Learning

- TensorFlow
- Keras
- CNN
- MobileNetV2
- Transfer Learning


## Computer Vision

- OpenCV
- Image Processing


## Frontend / Deployment

- Streamlit Cloud



---

# 📂 Project Structure

```
Vehicle-Classification-Streamlit

│
├── app.py

├── best_vehicle_model.h5

├── requirements.txt

├── README.md

```


---

# ⚙️ Installation


Clone repository:

```bash
git clone https://github.com/yourusername/Vehicle-Classification-Streamlit.git
```


Move into project:

```bash
cd Vehicle-Classification-Streamlit
```


Install dependencies:

```bash
pip install -r requirements.txt
```


---

# ▶️ Run Application


Start Streamlit:

```bash
streamlit run app.py
```


Open:

```
http://localhost:8501
```


---

# 🔍 Prediction Pipeline


1. Upload vehicle image


2. Image preprocessing:

- Resize image to 224 × 224
- Normalize pixels
- Convert image tensor


3. MobileNetV2 prediction


4. Confidence calculation


5. Display final result



Example:

```
Prediction:
Car

Confidence:
98.6%
```


---

# 📊 Prediction Output


Example:

| Class | Probability |
|---|---|
| Car | 98% |
| Bus | 1% |
| Truck | 1% |



---

# 🌐 Streamlit Deployment


Deployment platform:

## Streamlit Cloud


Steps:

1. Push project to GitHub

2. Open Streamlit Cloud

3. Connect repository

4. Select:

```
app.py
```

5. Deploy


Application URL:

```
https://your-project-name.streamlit.app
```


---

# 📦 Requirements


```
streamlit

tensorflow-cpu==2.17.0

numpy

opencv-python-headless

pillow
```


---

# 🔮 Future Improvements


- Real-time camera detection
- YOLO object detection integration
- More vehicle categories
- Larger training dataset
- Cloud API deployment
- Mobile application support


---

# 👨‍💻 Author


## Vishnu T Pillai


### Connect with me:


💼 LinkedIn:

https://www.linkedin.com/in/vishnu-t-pillai


💻 GitHub:

https://github.com/Vishnutpillai


---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.


<p align="center">

Built with ❤️ using Deep Learning, TensorFlow and Streamlit

</p>
