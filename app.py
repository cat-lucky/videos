from streamlit_ws_localstorage import injectWebsocketCode
from utils.animatedText import animated_text
from apps.editFile import editFile
from auth.login import login
from apps.main import main
import streamlit as st
import datetime
import uuid

if 'expiration_date' not in st.session_state:
  st.session_state['expiration_date'] = None
if 'password' not in st.session_state:
  st.session_state['password'] = None

def server():
  return injectWebsocketCode(hostPort='wsauthserver.supergroup.ai', uid=str(uuid.uuid1()))

def getPassword():
  conn = server()
  expiration_date_conn = conn.getLocalStorageVal("expiration_date")
  if expiration_date_conn is not None and expiration_date_conn:
    expiration_date = datetime.datetime.fromisoformat(expiration_date_conn)
    if datetime.datetime.now() < expiration_date:
      return conn.getLocalStorageVal("password")
  return None

def app():
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

if __name__ == "__main__":
  if st.session_state['password'] is None:
    st.session_state['password'] = getPassword()

  if st.session_state['password'] == st.secrets['SECRET_KEY']:
    app()
  else:
    conn = server()
    conn.setLocalStorageVal("password", None)
    conn.setLocalStorageVal("expiration_date", (datetime.datetime.now() - datetime.timedelta(days=10)).isoformat())
    login(conn)
