from apps.model import modelApp
from utils.randomColor import generate_random_colors
import streamlit as st
import gdown
import json
import random

def animated_text(text):
  colors = generate_random_colors(10)
  animated_text = "".join([f'<span style="color:{random.choice(colors)};">{char}</span>' for char in text])
  return animated_text

@st.cache_resource
def downloadContent():
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['google_drive']['SERVICE_ACCOUNT_FILE']}", 'credentials.json', quiet=False)

  gdown.download(f"https://drive.google.com/uc?id={st.secrets['data']['ACG']}", 'acg.json', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['data']['LAM']}", 'lam.json', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['data']['DATA']}", 'data.csv', quiet=False)

  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['LOGISTIC']}", 'logistic_regression.pkl', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['DECISION_TREE']}", 'decision_tree.pkl', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['RANDOM_FOREST']}", 'random_forest.pkl', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['SVM']}", 'support_vector_machine.pkl', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['KNN']}", 'k_nearest_neighbors.pkl', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['NAIVE_BAYES']}", 'naive_bayes.pkl', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['XGB']}", 'xgboost.pkl', quiet=False)
  gdown.download(f"https://drive.google.com/uc?id={st.secrets['models']['VOTING']}", 'voting_classifier.pkl', quiet=False)

downloadContent()

def loadContent(FILE):
  with open(f'{FILE.lower()}.json') as file:
    data = json.load(file)
  CATEGORIES = {item['category'] for item in data if item['category']}
  CATEGORY = st.selectbox("Choose a Category 🗂️", [None] + sorted(CATEGORIES), key="category_key")
  if CATEGORY:
    from apps.videos import showVideos
    showVideos(CATEGORY, f'{FILE.lower()}.json')
  else:
    st.info("Please select a category to watch the videos.", icon="ℹ️")

def videos():
  FILES = {"LIVE ACTION MOVIES": "LAM", "ANIMATED WORLD": "ACG", "ADD NEW DATA": "ADD"}
  choice = st.sidebar.selectbox("Select your choice", list(FILES.keys()), key="choice_key")
  if choice is not None:
    if FILES[choice] == "ADD":
      st.markdown(f"<h2 style='text-align: center;'>{animated_text(f'{choice.title()} 🌟')}</h2>", unsafe_allow_html=True)
      from apps.editFile import editFile
      editFile()
    else:
      st.markdown(f"<h2 style='text-align: center;'>{animated_text(f'{choice.title()} 🌟')}</h2>", unsafe_allow_html=True)
      loadContent(FILES[choice])
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 18px;'>Enjoy watching the videos! 🎉</div>", unsafe_allow_html=True)

  else:
    st.markdown(f"<h3 style='text-align: center;'>{animated_text('Please select a category to watch the videos! 🎉')}</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
  if 'password' not in st.session_state:
    st.session_state['password'] = None

  if st.session_state['password'] is not None and st.session_state['password'] == st.secrets['PASSWORD']:
    choiceA = st.sidebar.selectbox("Choose App/Model?", [None, 'App', 'Model'])
    if choiceA == 'App':
      videos()
    elif choiceA == 'Model':
      st.markdown(f"<h1 style='text-align: center;'>{animated_text(f'Welcome to Models 🌟')}</h1>", unsafe_allow_html=True)
      modelApp()
    else:
      st.markdown(f"<h1 style='text-align: center;'>{animated_text(f'Welcome to the application! 🌟')}</h1>", unsafe_allow_html=True)
      st.info("Select any option from the sidebar!", icon="ℹ️")

  else:
    st.markdown(f"<h3 style='text-align: center;'>{animated_text('Please Enter The Password! 🎉')}</h3>", unsafe_allow_html=True)
    password = st.text_input('Enter a valid password:', placeholder='password', type='password')
    if st.button("Submit Password") and password:
      st.session_state['password'] = password
      if password == st.secrets['PASSWORD']:
        st.toast("Correct Password! Starting App...", icon="✅")
        st.rerun()
      else:
        st.toast("Wrong Password! Please try again.", icon="🚨")
