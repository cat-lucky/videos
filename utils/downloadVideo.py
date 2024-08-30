import streamlit as st
import requests

def downloadVideo(url):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_name = url.split("/")[-1] + ".mp4"
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            return file_name
        else:
            st.error(f"Error downloading video: {response.status_code}")
    except Exception as e:
        st.error(f"Exception: {e}")
