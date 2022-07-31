import streamlit as st
from PIL import Image,ImageOps
import requests
import tensorflow as tf
from io import BytesIO


### Set page 
st.set_page_config(
    page_title="Khalisul_Akbar-Batch 10",
    page_icon="🏀",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://github.com/Khal0000",
        'About': "# This is my first dashboarb!!!"
    }
)

st.markdown("<h1 style='text-align: center; color:  #ff957f ;'>Types of Balls - Image Classification</h1>", unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#ff957f;background-color:#333;" /> """, unsafe_allow_html=True) 

col1, col2 = st.columns([0.5, 3])

# label = 'label'
with col1:
    source = st.select_slider("source :",options=['Url', 'local'], value='local')

with col2:
    if source == 'local':
        uploaded_file = st.file_uploader("Choose any ball image ...", type="jpg")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded image.', use_column_width=True)
            size = (128, 128)
            image = ImageOps.fit(image, size)
            x = tf.keras.preprocessing.image.img_to_array(image)
            x = x.tolist()

            URL = "https://h8-balls-backend.herokuapp.com/predict"
            data = {"image" : x ,
                "label" : 'M'}

            r = requests.post(URL, json=data)
            res = r.json()

            submit = st.button("Predict")
            if res['code'] == 200 and submit:
                st.markdown(f"<h6 style='text-align: left; color: white ; font-size: 130;'>Our Machine predicted that this is :</h6>", unsafe_allow_html=True)
                st.markdown(f"<h5 style='text-align: center; color: #34eb95; font-size: 50px;'>{res['result']['classes']}</h5>", unsafe_allow_html=True)
    else :
        url_input = st.text_input('copy and past the url here...', value="https://images.unsplash.com/photo-1614632537190-23e4146777db?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHx8&w=1000&q=80")
        
        if url_input is not None:
            response = requests.get(str(url_input))
            img = Image.open(BytesIO(response.content))
            st.image(img, caption='Uploaded image.', use_column_width=True)

            size = (128, 128)
            image = ImageOps.fit(img, size)
            x = tf.keras.preprocessing.image.img_to_array(image)
            x = x.tolist()

            URL = "https://h8-balls-backend.herokuapp.com/predict"
            data = {"image" : x ,
                "label" : 'M'}

            r = requests.post(URL, json=data)
            res = r.json()

            submit = st.button("Predict")
            if res['code'] == 200 and submit:
                st.markdown(f"<h6 style='text-align: left; color: white ; font-size: 130;'>Our Machine predicted that this is :</h6>", unsafe_allow_html=True)
                st.markdown(f"<h5 style='text-align: center; color: #34eb95; font-size: 50px;'>{res['result']['classes']}</h5>", unsafe_allow_html=True)

st.markdown("""<hr style="height:10px;border:none;color:#ff957f;background-color:#333;" /> """, unsafe_allow_html=True) 

