from utils.animatedText import animated_text
from apps.videos import showVideos
import streamlit as st
import gdown
import json

@st.cache_resource
def load_data(FILE):
    gdown.download(f"https://drive.google.com/uc?id={st.secrets[FILE]}", f'{FILE.lower()}.json', quiet=False)

def main(NAME, FILE):
    st.markdown(f"<h4 style='text-align: center;'>{animated_text(f'Welcome to {NAME.title()} 🌟')}</h4>", unsafe_allow_html=True)
    with open(f'{FILE.lower()}.json') as file:
        data = json.load(file)
    CATEGORIES = {item['category'] for item in data if item['category']}
    CATEGORY = st.selectbox("Choose a Category 🗂️", [None] + sorted(CATEGORIES), key="category_key")
    if CATEGORY:
        showVideos(CATEGORY, f'{FILE.lower()}.json')
    else:
        st.info("Please select a category to watch the videos.", icon="ℹ️")
