import streamlit as st
from frontend.components import render_hero, render_uploader, render_results
from frontend.sidebar import render_sidebar_col
from backend.database import get_by_id
import base64

def render_footer():
    try:
        logo_b64 = base64.b64encode(open("qubrid_logo.png","rb").read()).decode()
        img_tag  = f'<img src="data:image/png;base64,{logo_b64}" style="height:13px;width:13px;object-fit:contain;border-radius:2px;">'
    except Exception:
        img_tag = "⚡"
    st.markdown(
        f'<div class="footer-badge">{img_tag} Powered by Qubrid AI</div>',
        unsafe_allow_html=True
    )

def render_main_view():
    is_open = st.session_state.get("sidebar_open", True)

    if is_open:
        sidebar_col, main_col = st.columns([1, 3.2], gap="medium")
    else:
        sidebar_col, main_col = st.columns([0.10, 5], gap="small")

    with sidebar_col:
        render_sidebar_col()

    with main_col:
        render_hero()

        if "active_view" not in st.session_state:
            st.session_state["active_view"] = "new"

        view = st.session_state["active_view"]

        if view == "new":
            render_uploader()
        elif view == "result":
            render_results()
        elif view == "history":
            data = get_by_id(st.session_state.get("history_id"))
            if data:
                render_results(result=data["result"], filename=data["filename"])
            else:
                st.warning("Transcript not found.")
                st.session_state["active_view"] = "new"
                st.rerun()

    render_footer()