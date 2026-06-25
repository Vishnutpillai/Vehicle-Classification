import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
from keras.utils import custom_object_scope
import time


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Vehicle AI Detector",
    page_icon="🚗",
    layout="wide"
)


# -------------------------------
# Custom CSS
# -------------------------------

st.markdown("""

<style>


.main{

background-color:#f7f9fc;

}


.title{

font-size:45px;
font-weight:700;
text-align:center;
color:#1f2937;

}


.subtitle{

text-align:center;
font-size:18px;
color:#6b7280;

}



.card{

background:white;
padding:30px;
border-radius:20px;
box-shadow:0px 5px 20px rgba(0,0,0,0.1);

}



.result{

font-size:30px;
font-weight:bold;
text-align:center;

}



.vehicle{

color:#059669;

}



.nonvehicle{

color:#dc2626;

}



</style>

""", unsafe_allow_html=True)



# -------------------------------
# Load Model
# -------------------------------




@st.cache_resource
def load_model():

    model=tf.keras.models.load_model(
    "best_vehicle_model.h5",
    compile=False
    )

    return model


model = load_model()



# -------------------------------
# Classes
# -------------------------------


class_names=[

"Bicycle",
"Bus",
"Car",
"Ships",
"Trains",
"Truck",
"Aeroplane",
"Motorcycle"

]



# -------------------------------
# Header
# -------------------------------


st.markdown(
"""
<div class="title">

🚗 Vehicle AI Classification

</div>

<p class="subtitle">

Deep Learning powered vehicle detection using MobileNetV2

</p>

""",

unsafe_allow_html=True
)



st.write("")



# -------------------------------
# Upload Section
# -------------------------------


uploaded_file=st.file_uploader(

"Upload Vehicle Image",

type=["jpg","jpeg","png"]

)



if uploaded_file:


    col1,col2=st.columns(2)



    with col1:


        image=Image.open(uploaded_file)


        st.image(

            image,

            caption="Uploaded Image",

            use_container_width=True

        )



    with col2:


        st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
        )


        with st.spinner("AI analyzing image..."):


            time.sleep(1)


            img=np.array(image)



            img=cv2.resize(

                img,

                (224,224)

            )


            img=img/255.0



            img=np.expand_dims(

                img,

                axis=0

            )



            prediction=model.predict(img)



            index=np.argmax(prediction)


            confidence=float(

                np.max(prediction)

            )



        threshold=0.70



        if confidence < threshold:


            result="Non Vehicle"


            st.markdown(

            f"""

            <div class="result nonvehicle">

            ❌ {result}

            </div>

            """,

            unsafe_allow_html=True

            )



        else:


            result=class_names[index]


            st.markdown(

            f"""

            <div class="result vehicle">

            ✅ {result}

            </div>

            """,

            unsafe_allow_html=True

            )



        st.write("")



        st.metric(

            "Confidence",

            f"{confidence*100:.2f}%"

        )



        st.progress(

            confidence

        )



        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )


# -------------------------------
# Footer
# -------------------------------


st.markdown(

"""

<br><br>

<center>

Powered by TensorFlow + MobileNetV2 + Deep Learning

</center>

""",

unsafe_allow_html=True

)