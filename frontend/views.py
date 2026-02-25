import streamlit as st
from frontend.components import render_editor, render_hero, render_uploader
from backend.database import get_transcript_by_id

def render_main_view():
    render_hero()

    if "active_view" not in st.session_state:
        st.session_state["active_view"] = "new"

    if st.session_state["active_view"] == "new":
        render_uploader()

    elif st.session_state["active_view"] == "result":
        render_editor(
            st.session_state["res_script"], 
            st.session_state["res_name"], 
            st.session_state.get("res_path")
        )
    
    elif st.session_state["active_view"] == "history":
        data = get_transcript_by_id(st.session_state["current_id"])
        if data: 
            render_editor(data["script"], data["filename"])