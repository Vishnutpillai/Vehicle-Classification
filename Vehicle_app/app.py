import os
from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

# Load Trained Model

model = tf.keras.models.load_model(
    "best_vehicle_model.h5")

class_names = [

    "Bicycle",
    "Bus",
    "Car",
    "Ships",
    "Trains",
    "Truck",
    "aeroplane",
    "motorcycle"
    ]
UPLOAD_FOLDER = os.path.join(app.root_path,"static","uploads")


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True)

# Home Page

@app.route("/")

def home():
    return render_template(
        "home.html")

# Prediction Route

@app.route("/predict",
methods=["POST"])

def predict():
    image = request.files["image"]
    filename = image.filename
    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename)
    image.save(path)

    # CV preprocessing
    img=cv2.imread(path)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=cv2.resize(img,(224,224))
    img=img/255.0
    img=np.expand_dims(img,axis=0)

    # MobileNetV2 Prediction
    prediction=model.predict(img)
    index=np.argmax(prediction)
    confidence=np.max(prediction)
    thers=0.70
    if confidence < thers:
        result='Non Vehicle'
    else:
        result=class_names[index]
    confidence=round(confidence*100,2)

    return render_template(
        "prediction.html",
        prediction=result,
        confidence=confidence,
        image='uploads/'+filename
    )


if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )