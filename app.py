import streamlit as st
from config.settings import config

# 1. Page Config MUST be the very first command
st.set_page_config(
    page_title="Deep Diarizer Studio",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Prep environment paths
config.setup_directories()

# 3. Imports
from backend.database import init_db
from frontend.styles import load_css
from frontend.sidebar import render_sidebar
from frontend.views import render_main_view

def main():
    init_db()
    load_css()
    render_sidebar()
    render_main_view()

if __name__ == "__main__":
    main()