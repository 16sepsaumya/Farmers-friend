import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
import tensorflow as tf

model = load_model('plant_disease_model.h5')
                    
CLASS_NAMES = ('Tomato-Bacterial_spot', 'Potato-Barly blight', 'Corn-Common_rust')

st.title("Plant Disease Detection")
st.markdown("Upload an image of the plant leaf")

plant_image = st.file_uploader("Choose an image...", type = "jpg")
submit = st.button('predict Disease')

if submit:
    if plant_image is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray (bytearray(plant_image.read()), dtype = np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)
        
        opencv_image = cv2.resize(opencv_image, (256, 256))
        
        opencv_image.shape = (1, 256, 256, 3)
        
        Y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(Y_pred)]
        st.title(str("This is "+result.split('-')[0]+ " leaf with " +  result.split('-')[1]))