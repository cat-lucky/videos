# Animations, Cartoons & Graphics
from apps.pages.videos import showVideos
import streamlit as st
import random
import gdown
import json

@st.cache_data
def load_data():
    try:
        gdown.download(f"https://drive.google.com/uc?id={st.secrets['ACG']}", 'acg.json', quiet=False)
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}", icon="🚫")
        return False

def animated_text(text):
    colors = ["#ff6347", "#ffa500", "#ffff00", "#32cd32", "#00ced1", "#1e90ff", "#9370db"]
    animated_text = "".join([f'<span style="color:{random.choice(colors)};">{char}</span>' for char in text])
    return animated_text

st.set_page_config(page_title="Animated Worlds", page_icon="🌟", layout="wide")
st.markdown(f"<h1 style='text-align: center;'>{animated_text('Welcome to Animated Worlds 🌟')}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>Explore your favorite animated videos 🎥✨</h2>", unsafe_allow_html=True)
st.markdown(f"<h6 style='text-align: center;'>Dive into a world of animation, where imagination meets reality. Choose your favorite category and start watching! 🎬</h6>", unsafe_allow_html=True)

if load_data():
    with open('acg.json') as file:
        data = json.load(file)
    CATEGORIES = set([item['category'] if item['category'] != "" else None for item in data])
    CATEGORIES.add(None)
    CATEGORY = st.selectbox("Choose a Category 🗂️", list(CATEGORIES))

    if CATEGORY:
        st.markdown(f"<div style='text-align: center; font-size: 24px;'>You selected: <b>{CATEGORY} 🍿</b></div>", unsafe_allow_html=True)
        showVideos(CATEGORY, 'acg.json')
    else:
        st.info("Please select a category to view the videos.", icon="ℹ️")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 18px;'>Enjoy watching! 🎉</div>", unsafe_allow_html=True)

else:
    st.warning("Failed to load data. Please try again later.", icon="⚠️")
