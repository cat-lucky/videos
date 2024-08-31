from streamlit_local_storage import LocalStorage
from utils.animatedText import animated_text
from auth.login import login
from apps.main import main
import streamlit as st
import datetime

localS = LocalStorage()

def is_credentials_valid():
  if localS.getAll():
    expiration_date = datetime.datetime.fromisoformat(localS.getItem("expiration_date"))
    if datetime.datetime.now() < expiration_date:
      return True
  return False

def app():
  st.markdown(f"<h1 style='text-align: center;'>{animated_text(f'Welcome to Videos World 🌟')}</h1>", unsafe_allow_html=True)
  FILES = {"ANIMATED WORLD": "ACG", "LIVE ACTION MOVIES": "LAM"}
  choice = st.selectbox("Select your choice", [None] + list(FILES.keys()), key="choice")
  if choice is not None:
    main(choice, FILES[choice])
  else:
    st.info("Please select a category to watch the videos.", icon="ℹ️")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 18px;'>Enjoy watching the videos! 🎉</div>", unsafe_allow_html=True)

if __name__ == "__main__":
  if is_credentials_valid():
    password = localS.getItem("password")
    if password is not None:
      if password == st.secrets['SECRET_KEY']:
        app()
      else:
        if localS.getAll():
          localS.deleteAll()
    else:
      login()
  else:
    if localS.getAll():
      localS.deleteAll()
    login()
