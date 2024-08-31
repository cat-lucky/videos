from streamlit_local_storage import LocalStorage
import streamlit as st
import datetime

localS = LocalStorage()

def save_credentials(password, days):
  expiration_date = datetime.datetime.now() + datetime.timedelta(days=days)

  itemKey="password"
  itemValue=f'{password}'
  localS.setItem(itemKey, itemValue, key="password_key")

  itemKey="expiration_date"
  itemValue=f"{expiration_date.isoformat()}"
  localS.setItem(itemKey, itemValue, key="expiration_date_key")

def login():
  st.header("Login")
  col1, col2 = st.columns(2)
  with col1:
    name = st.text_input("Enter your name", key="name")
  with col2:
    password = st.text_input("Enter your secret key", type="password", key="secret_key")
  remember_me = st.checkbox("Remember me for 30 days")

  if st.button("Start Application"):
    if password == st.secrets['SECRET_KEY']:
      if remember_me:
        save_credentials(password, 30)
      else:
        save_credentials(password, 2)
      st.rerun()
    st.error("Incorrect Secret Key.", icon="🚨")
