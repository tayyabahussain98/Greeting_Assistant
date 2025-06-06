import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

genai.configure(api_key = gemini_api_key)

st.set_page_config('💖  Greeting Assistant 💖')

st.title('🫂🌙Eid Ul Adha Greeting Assistant🐄🐪')

name = st.text_input('🎉 Enter your name')

if st.button('Submit'):
    if name:
        try:
            model = genai.GenerativeModel(model_name = 'models/gemini-2.0-flash')
            prompt = f'Write a heartful Eid-ul-Adha greeting from someone named {name}. The message should be warm, respectful, and suitable to send to family and friends in Roman Urdu.'

            with st.spinner('Generating your Eid greeting... 🧕🕌'):
                response = model.generate_content(prompt)

            st.markdown('### 🌙 Your Eid Greeting')
            st.success(response.text)

        except Exception as e:
            st.error(f'Somthing went wrong: {e}')


st.markdown('---')
st.write('Made with 🤍 by Tayyaba Hussain')