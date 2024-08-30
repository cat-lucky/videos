import streamlit as st

def dashboard():
    st.set_page_config(page_title="Streamlit Videos World", page_icon="🌍")
    st.markdown("<h1 style='text-align: center;'>🎥 Welcome to the Streamlit Videos World! 🌍</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 18px;'>
        This is a simple Streamlit app that showcases videos from different websites. 
        You can watch videos, download them, visit the website, and watch more videos from the website.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div>
        <p>🔐 To get started, you can log in or sign up to access the dashboard.</p>
        <p>👤 If you are already logged in, you can view your profile and log out.</p>
        <p>🎬 You can also view videos from different categories by clicking on the respective links in the sidebar.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.logged_in:
        st.markdown("""
        <h2>✨ All the Categories are: ✨</h2>
        <h5>✨ Animations, Cartoons & Graphics ✨</h5>
        <ul style='list-style-type: none;'>
            <li>🔞 Hentai</li>
        </ul>

        <h5>✨ Live Action Movies ✨</h5>
        <ul style='list-style-type: none;'>
            <li>🔪 Brutal</li>
            <li>👩‍❤️‍👨 Cheat</li>
            <li>👨‍👩‍👧 Family</li>
            <li>🧹 Maid</li>
            <li>🏫 School</li>
            <li>👩‍💼 Secretary</li>
            <li>👩‍❤️‍👨 Sister</li>
            <li>👦 StepBrother</li>
            <li>👩🏻‍🦰 StepMom</li>
            <li>👩🏻‍🦰 StepSister</li>
            <li>👤 Stranger</li>
            <li>🦺 Stuck</li>
        </ul>
        <hr />
        """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 18px;'>Enjoy watching videos! 🍿</p>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; color: gray;'>
        Note: This app is for personnel purposes only and does not advertisement any videos.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: center;'>
        You can also access the Vercel website: 
        <a href='https://main-gallery.vercel.app/' target='_blank'>click here</a> 🌐
    </p>
    """, unsafe_allow_html=True)

    if st.session_state.logged_in:
        st.markdown("""<p style='text-align: center;'>Made with ❤️ by Lucky</p>""", unsafe_allow_html=True)

dashboard()
