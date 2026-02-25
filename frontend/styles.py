import streamlit as st

def load_css():
    st.markdown("""
    <style>
        .stApp { background-color: #0B0E14; }
        header {visibility: hidden;}
        .block-container { padding-top: 2rem; max-width: 1000px; }
        
        [data-testid="stSidebar"] { 
            background-color: #11151C; 
            border-right: 1px solid #1F2937; 
        }
        
        .hero-title { font-size: 3rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0px; padding-bottom: 0px; }
        .hero-subtitle { color: #94A3B8; font-size: 1.1rem; margin-top: 5px; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)