from utils.animatedText import animated_text
from apps.editFile import editFile
from apps.main import main
from apps.model import modelApp
import streamlit as st

def videos():
  st.markdown(f"<h1 style='text-align: center;'>{animated_text(f'Welcome to Videos World 🌟')}</h1>", unsafe_allow_html=True)
  FILES = {"ANIMATED WORLD": "ACG", "LIVE ACTION MOVIES": "LAM", "ADD NEW DATA": "AND"}
  choice = st.selectbox("Select your choice", [None] + list(FILES.keys()), key="choice_key")
  if choice is not None:
    if FILES[choice] == "AND":
      editFile()
    else:
      main(choice, FILES[choice])
  else:
    st.info("Please select a category to watch the videos.", icon="ℹ️")
  st.markdown("<hr>", unsafe_allow_html=True)
  st.markdown(f"<div style='text-align: center; font-size: 18px;'>Enjoy watching the videos! 🎉</div>", unsafe_allow_html=True)

def app():
  st.title("Welcome to the application!")
  choiceA = st.selectbox("Choose App/Model?", ['App', 'Model'])
  if choiceA == 'App':
    videos()
  else:
    modelApp()

if __name__ == "__main__":
  if 'password' not in st.session_state:
    st.session_state['password'] = None

  if st.session_state['password'] is None or st.session_state['password'] != st.secrets['PASSWORD']:
    password = st.text_input('Enter a valid password:', placeholder='password', type='password')
    if st.button("Submit Password") and password:
      st.session_state['password'] = password
      if password == st.secrets['PASSWORD']:
        st.toast("Correct Password! Starting App...", icon="✅")
        app()
      else:
        st.toast("Wrong Password! Please try again.", icon="🚨")
  else:
    st.toast("Application Started!", icon="😃")
    app()
