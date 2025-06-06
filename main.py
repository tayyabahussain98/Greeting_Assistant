import streamlit as st
import google.generativeai as genai
import os

# Set page config
st.set_page_config(page_title="💖 Eid Greeting Assistant", page_icon="🌙")

# Load API key from secrets (for Streamlit Cloud)
gemini_api_key = st.secrets.get("GEMINI_API_KEY", None)

# Configure Gemini
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)
else:
    st.error("API Key not found! Please set GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# Title
st.title('🫂🌙 Eid Ul Adha Greeting Assistant 🐄🐪')

# Input
name = st.text_input('🎉 Enter your name')

# Button
if st.button('Generate Greeting'):
    if name:
        try:
            model = genai.GenerativeModel(model_name='models/gemini-2.0-flash')

            # Short & fast prompt
            prompt = f"Write a short, warm Eid-ul-Adha greeting in Roman Urdu from {name}. Max 2 lines, friendly and respectful."

            with st.spinner("Generating your Eid greeting... 🌙✨"):
                response = model.generate_content(prompt)

            # Show greeting
            st.markdown('### 🌙 Your Eid Greeting:')
            st.success(response.text)

        except Exception as e:
            st.error(f'Something went wrong: {e}')
    else:
        st.warning('Please enter your name first.')

# Footer
st.markdown("---")
st.caption("Made with 🤍 by Tayyaba Hussain")
