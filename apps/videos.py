import streamlit as st
import webbrowser

# Importing the helper functions
from data.loadData import loadData
from utils.calculateTime import calculateTime
from utils.downloadVideo import downloadVideo
from utils.randomColor import randomColor

def showVideos(CATEGORY, FILE_PATH):
    DATA = loadData(CATEGORY, FILE_PATH)
    INDEX = 1
    for item in DATA:
        st.markdown(f"---")
        
        st.write(f"### 🌟 Featured Video {INDEX}")
        st.write(f'**Video ID:** {FILE_PATH}/{item["ID"]}')

        if item['imageURL'] != "":
            st.image(item['imageURL'], caption=item['name'], use_column_width=True)
        else:
            st.markdown(f'<iframe src="{item["iFrameURL"]}" width="100%" height="500" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            st.write(f"#### <span style='color:{randomColor()};'>{item['name']}</span>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(f"⏳ **Duration:** <span style='color:{randomColor()};'>{calculateTime(item['timeStamp'])}</span>", unsafe_allow_html=True)
        with col2:
            tags = " / ".join([f'<span style="color:{randomColor()};">{tag}</span>' for tag in item['tags']])
            st.markdown(f"🏷️ **Tags:** {tags or 'No tags available'}", unsafe_allow_html=True)
        with col3:
            boys = " / ".join([f'<span style="color:{randomColor()};">{name}</span>' for name in item['boyName']])
            st.markdown(f"🎭 **Heros:** {boys or 'No names available'}", unsafe_allow_html=True)
        with col4:
            girls = " / ".join([f'<span style="color:{randomColor()};">{name}</span>' for name in item['girlName']])
            st.markdown(f"🌟 **Stars:** {girls or 'No names available'}", unsafe_allow_html=True)

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            if item['iFrameURL'] != "":
                st.markdown(f"""
                    <a href="{item['iFrameURL']}" target="_blank">
                        <button style="padding: 10px; width: 100%; border-radius: 10px; background-color: transparent; border: 1px solid salmon;">▶️ Watch Instantly</button>
                    </a>
                """, unsafe_allow_html=True)

        with col6:
            if item['videoURL'] != "":
                st.markdown(f"""
                    <a href="{item['videoURL']}" target="_blank">
                        <button style="padding: 10px; width: 100%; border-radius: 10px; background-color: transparent; border: 1px solid salmon;">📺 Full Video</button>
                    </a>
                """, unsafe_allow_html=True)

        with col7:
            if item['websiteURL'] != "":
                st.markdown(f"""
                    <a href="{item['websiteURL']}" target="_blank">
                        <button style="padding: 10px; width: 100%; border-radius: 10px; background-color: transparent; border: 1px solid salmon;">🔍 More Videos</button>
                    </a>
                """, unsafe_allow_html=True)

        with col8:
            if item['downloadURL'] != "":
                file_name = downloadVideo(item['downloadURL'])
                if file_name:
                    with open(file_name, "rb") as file:
                        st.download_button(label="⬇️ Download Video", data=file, file_name=file_name, key=f"download_btn_{item['ID']}_{item['timeStamp']}")

        INDEX += 1
