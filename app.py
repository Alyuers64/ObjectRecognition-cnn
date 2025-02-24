import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('C:/Users/lenovo/Documents/py-objek-recog/models/cifar10_cnn_model.h5')

cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def prepare_image(image):
    img = image.resize((32, 32))
    img = np.array(img)
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    return img

st.title("Prediksi Gambar")
st.write("Upload gambar!")

uploaded_image = st.file_uploader("Pilih gambar", type=["jpg", "png"])

if uploaded_image is not None:
    img = Image.open(uploaded_image)
    st.image(img, caption='Gambar yang diupload', use_container_width=True)

    prepared_img = prepare_image(img)
    predictions = model.predict(prepared_img)
    predicted_class = np.argmax(predictions, axis=1)
    
    st.write(f"Gambar ini termasuk kategori: {cifar10_classes[predicted_class[0]]}")
