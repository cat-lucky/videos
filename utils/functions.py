import streamlit as st
from auth.profile import profile

def logout():
  if st.session_state.logged_in:
    profile()
    if st.button("Log out"):
      st.session_state.logged_in = False
      st.rerun()

logout_page = st.Page(logout, title="My Profile", icon=":material/account_circle:")
dashboard = st.Page("apps/dashboard.py", title="Dashboard", icon=":material/dashboard:")

# Pages
acg = st.Page("apps/pages/acg.py", title="Animated Worlds", icon=":material/movie_creation:")
lam = st.Page("apps/pages/lam.py", title="Live Action Movies", icon=":material/movie_creation:")

# Loading All The Pages After Login 
def load_functions():
  pages = {
    "": [dashboard],
    "Account": [logout_page],
    "Videos": [acg, lam],
  }
  return pages
