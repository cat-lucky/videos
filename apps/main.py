from utils.animatedText import animated_text
from apps.videos import showVideos
import streamlit as st
import gdown
import json

def load_data(FILE):
    try:
        gdown.download(f"https://drive.google.com/uc?id={st.secrets[FILE]}", f'{FILE.lower()}.json', quiet=False)
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}", icon="🚫")
        return False

def main(NAME, FILE):
    st.markdown(f"<h4 style='text-align: center;'>{animated_text(f'Welcome to {NAME.title()} 🌟')}</h4>", unsafe_allow_html=True)

    if load_data(FILE):
        with open(f'{FILE.lower()}.json') as file:
            data = json.load(file)

        CATEGORIES = {item['category'] for item in data if item['category']}
        CATEGORY = st.selectbox("Choose a Category 🗂️", [None] + sorted(CATEGORIES))

        if CATEGORY:
            showVideos(CATEGORY, f'{FILE.lower()}.json')
        else:
            st.info("Please select a category to watch the videos.", icon="ℹ️")

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center; font-size: 18px;'>Enjoy watching the videos! 🎉</div>", unsafe_allow_html=True)

    else:
        st.warning("Failed to load data. Please try again later.", icon="⚠️")
