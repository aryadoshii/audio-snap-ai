import streamlit as st
from backend.database import get_history

def render_sidebar():
    with st.sidebar:
        if st.button("✨ New Transcription", use_container_width=True, type="primary"):
            st.session_state["active_view"] = "new"
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.caption("RECENT ACTIVITY")
        
        history = get_history()
        if not history:
            st.caption("No recent transcripts.")
        
        for t_id, fname, t_time in history:
            display_name = (fname[:20] + '...') if len(fname) > 20 else fname
            if st.button(f"💬 {display_name}", key=f"hist_{t_id}", use_container_width=True):
                st.session_state["active_view"] = "history"
                st.session_state["current_id"] = t_id
                st.rerun()