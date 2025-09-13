import streamlit as st
from pathlib import Path
import importlib.util

# --- PAGE SETUP ---
st.set_page_config(
    layout="wide",
    page_title="EcoSnap",
    page_icon=":earth_africa:",
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("EcoSnap Navigation")
page_choice = st.sidebar.radio(
    "Go to",
    ["Home", "EcoSnap", "EcoAlt", "EcoTalk"]
)

# --- HELPER FUNCTION TO LOAD PAGES ---
def load_page(page_path):
    """
    Dynamically load a Python file as a module and run it.
    """
    if not Path(page_path).exists():
        st.error(f"Page not found: {page_path}")
        return
    spec = importlib.util.spec_from_file_location("module.name", page_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

# --- PAGE ROUTING ---
if page_choice == "Home":
    load_page("ch/home.py")
elif page_choice == "EcoSnap":
    load_page("ch/EcoSnap.py")
elif page_choice == "EcoAlt":
    load_page("ch/EcoAlt.py")
elif page_choice == "EcoTalk":
    load_page("ch/EcoTalk.py")

# --- FOOTER / CREDITS ---
st.sidebar.markdown("---")
st.sidebar.markdown(
    '''
    Created by EcoSnap Team ✨<br>
    <img src="https://img.shields.io/badge/EcoSnap-%F0%9F%8C%BF-32CD32?labelColor=2F4F4F" alt="EcoSnap">
    ''', unsafe_allow_html=True
)

