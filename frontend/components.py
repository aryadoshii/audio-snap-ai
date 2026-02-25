import streamlit as st
import pandas as pd
import os
from config.settings import config
from backend.graph import app_graph
from backend.database import save_transcript

def render_hero():
    st.markdown('<p class="hero-title">Deep Diarizer</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Transform raw audio into structured, speaker-aware intelligence.<br><span style="color: #6366F1;">Powered by Whisper-v3 on Qubrid Neural Cloud.</span></p>', unsafe_allow_html=True)

def render_uploader():
    with st.container(border=True):
        uploaded_file = st.file_uploader("Upload Audio (Max 25MB recommended)", type=["mp3", "wav", "m4a"])
        
        if uploaded_file:
            t_path = config.INPUT_DIR / uploaded_file.name
            with open(t_path, "wb") as f: f.write(uploaded_file.getbuffer())
            
            st.audio(uploaded_file)
            
            if st.button("Analyze Audio", use_container_width=True, type="primary"):
                with st.spinner("Extracting intelligence..."):
                    res = app_graph.invoke({"audio_path": str(t_path)})
                    
                    if "Error" in res.get("status", ""):
                        st.error(res['status'])
                    else:
                        script = res.get("script_segments", [])
                        save_transcript(uploaded_file.name, script)
                        
                        st.session_state.update({
                            "active_view": "result",
                            "res_script": script,
                            "res_name": uploaded_file.name,
                            "res_path": str(t_path)
                        })
                        st.rerun()

def render_editor(script_data, filename, audio_path=None):
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**Source:** `{filename}`")
        with col2:
            if not (audio_path and os.path.exists(audio_path)):
                st.caption("🔒 Archived (Text Only)")
        
        if audio_path and os.path.exists(audio_path):
            st.audio(audio_path)

    with st.container(border=True):
        st.markdown("**Transcript Editor**")
        df = pd.DataFrame(script_data)
        edited_df = st.data_editor(
            df,
            column_config={
                "timestamp": st.column_config.TextColumn("Time", disabled=True),
                "speaker": st.column_config.SelectboxColumn("Speaker", options=["Host", "Guest", "Speaker 1", "Speaker 2"]),
                "text": st.column_config.TextColumn("Content", width="large")
            },
            use_container_width=True, hide_index=True, height=500
        )
        st.download_button("⬇️ Export to CSV", edited_df.to_csv(index=False), f"{filename}.csv", "text/csv")