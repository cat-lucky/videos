import streamlit as st
import datetime

def save_credentials(localS, password, days):
  expiration_date = datetime.datetime.now() + datetime.timedelta(days=days)

  try:
    localS.setItem("password", str(password), key="password_key")
  except Exception as e:
    st.error(f'Error saving password: {e}', icon="🚨")

  try:
    localS.setItem("expiration_date", expiration_date.isoformat(), key="expiration_date_key")
  except Exception as e:
    st.error(f'Error saving expiration date: {e}', icon="🚨")

def login(localS):
  st.header("Login")
  col1, col2 = st.columns(2)
  with col1:
    name = st.text_input("Enter your name", key="name_key")
  with col2:
    password = st.text_input("Enter your secret key", type="password", key="secret_key")
  remember_me = st.checkbox("Remember me for 30 days", value=False, key="remember_me_key")

  if st.button("Start Application", key="start_app_btn_key"):
    if password == st.secrets['SECRET_KEY']:
      days = 30 if remember_me else 2
      save_credentials(localS, password, days)
      st.success(f"Credentials Saved for {days}!", icon="✅")
      st.rerun()
    st.error("Incorrect Secret Key.", icon="🚨")
