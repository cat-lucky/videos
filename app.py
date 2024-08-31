from streamlit_local_storage import LocalStorage
from utils.animatedText import animated_text
from apps.main import main
import streamlit as st
import datetime

localS = LocalStorage()

def save_credentials(password, days):
  expiration_date = datetime.datetime.now() + datetime.timedelta(days=days)
  localS.setItem(itemKey="password", itemValue=f'{password}')
  localS.setItem(itemKey="expiration_date", itemValue=f"{expiration_date.isoformat()}")

def is_credentials_valid():
  if localS.getAll():
    expiration_date = datetime.datetime.fromisoformat(localS.getItem("expiration_date"))
    if datetime.datetime.now() < expiration_date:
      return True
  return False

def login():
  st.header("Login")
  col1, col2 = st.columns(2)
  with col1:
    name = st.text_input("Enter your name", key="name")
  with col2:
    password = st.text_input("Enter your secret key", type="password", key="password")
  remember_me = st.checkbox("Remember me for 30 days")

  if st.button("Start Application"):
    if password == st.secrets['SECRET_KEY']:
      if remember_me:
        save_credentials(password, 30)
      else:
        save_credentials(password, 2)
      st.rerun()
    st.error("Incorrect Secret Key.", icon="🚨")

def app():
  st.markdown(f"<h1 style='text-align: center;'>{animated_text(f'Welcome to Videos World 🌟')}</h1>", unsafe_allow_html=True, key="h1")
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
