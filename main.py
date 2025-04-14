import streamlit as st



# --- PAGE SETUP ---
st.set_page_config(
    
    layout="wide",
    page_title="EcoSnap",
    page_icon=":earth_africa:",
)
#Define pages
about_page = st.Page(
    "ch/home.py",
    title="Home",
    icon="🏠",
    default=True,
)
project_1_page = st.Page(
    "ch/EcoSnap.py",
    title="EcoSnap",
    icon="📸",
)
project_2_page = st.Page(
    "ch/EcoAlt.py",
    title="EcoAlt",
    icon="🌱",
)
project_3_page = st.Page(
    "ch/EcoTalk.py",
    title="EcoTalk",
    icon="🗣️",
)

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown(
    '''
    Created by EcoSnap Team ✨<br>
    <img src="https://img.shields.io/badge/EcoSnap-%F0%9F%8C%BF-32CD32?labelColor=2F4F4F" alt="EcoSnap">
    </a>
    ''', unsafe_allow_html=True
)



pg.run()  # Run navigation outside of the sidebar context
