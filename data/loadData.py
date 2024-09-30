import streamlit as st
import json

@st.cache_resource
def loadData(category, file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
            FILTERED_DATA = []
            for item in data:
                if item['category'] == category:
                    FILTERED_DATA.append(item)
    except FileNotFoundError:
        st.error("JSON file not found.")
        st.stop()
    except json.JSONDecodeError:
        st.error("Error decoding JSON.")
        st.stop()
    return FILTERED_DATA
