import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from workflow import app_graph

# 1. Load Environment Variables immediately
load_dotenv()

# Check for Key
api_key = os.getenv("QUBRID_API_KEY")

# Configure Page
st.set_page_config(
    page_title="Deep Diarizer", 
    page_icon="🎙️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Enhanced UI (Glassmorphism & Gradients) ---
st.markdown("""
<style>
    /* Main Background with subtle gradient */
    .stApp {
        background: linear-gradient(to bottom right, #0e1117, #131720);
        color: #e0e0e0;
    }
    
    /* Glassmorphism Card Style */
    .glass-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* Header Styling */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
        color: #ffffff;
    }
    
    /* Custom Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #FF4B4B 0%, #FF9056 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        color: white;
    }
    
    /* Hide the default file uploader border to make it look cleaner */
    [data-testid='stFileUploader'] {
        width: 100%;
    }
    .stDataFrame {
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("🎛️ Controls")
    
    # Status Indicator
    if api_key:
        st.success("✅ API Key Loaded")
    else:
        st.error("❌ API Key Missing")
        st.caption("Please check your `.env` file.")
    
    st.markdown("---")
    st.markdown("""
    ### About
    **Deep Diarizer** uses **Whisper-Large-v3** to generate high-fidelity transcripts with timestamps.
    
    **How to use:**
    1. Upload Audio
    2. Process
    3. Assign Speakers
    4. Export
    """)
    
    st.markdown("---")
    st.caption(f"Powered by Qubrid AI")

# --- Main Content ---

# Title Section
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🎙️ Deep Diarizer")
    st.markdown("##### *Speaker-Aware Transcription Studio*")

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Main Logic
if not api_key:
    st.warning("⚠️ **System Halted:** `QUBRID_API_KEY` not found in `.env` file.")
    st.stop()

# Glass Container for Upload
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.subheader("1. Source Material")
uploaded_file = st.file_uploader("Drop your audio file here (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    # Save file temporarily
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Layout: Audio Player on Left, Action Button on Right
    c1, c2 = st.columns([2, 1])
    with c1:
        st.audio(uploaded_file)
    with c2:
        st.markdown("<br>", unsafe_allow_html=True) # Spacer
        process_btn = st.button("✨ Start Processing", use_container_width=True)
    
    if process_btn:
        with st.status("🚀 Processing Workflow...", expanded=True) as status:
            st.write("🔌 Connecting to Qubrid Neural Cloud...")
            
            # Run the Graph
            inputs = {"audio_path": temp_path, "status": "Starting"}
            
            try:
                # We invoke the graph
                st.write("🎧 Transcribing Audio (Whisper-v3)...")
                result = app_graph.invoke(inputs)
                
                # Check results
                if "Error" in result.get("status", ""):
                    status.update(label="❌ Failed", state="error")
                    st.error(result["status"])
                else:
                    status.update(label="✅ Completed", state="complete")
                    
                    # --- Results Section ---
                    st.markdown("---")
                    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                    st.subheader("📝 Script Editor")
                    
                    script_data = result.get("script_segments", [])
                    
                    if script_data:
                        df = pd.DataFrame(script_data)
                        
                        # Interactive Editor
                        edited_df = st.data_editor(
                            df,
                            column_config={
                                "timestamp": st.column_config.TextColumn(
                                    "Time", width="small", disabled=True
                                ),
                                "speaker": st.column_config.SelectboxColumn(
                                    "Speaker",
                                    options=["Host", "Guest", "Speaker 1", "Speaker 2"],
                                    required=True,
                                    width="medium"
                                ),
                                "text": st.column_config.TextColumn(
                                    "Transcript", width="large"
                                )
                            },
                            use_container_width=True,
                            hide_index=True,
                            height=500
                        )
                        
                        # Download Section
                        st.markdown("<br>", unsafe_allow_html=True)
                        col_d1, col_d2 = st.columns([1, 4])
                        with col_d1:
                            csv = edited_df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                "⬇️ Download CSV",
                                csv,
                                "transcript.csv",
                                "text/csv",
                                use_container_width=True
                            )
                    else:
                        st.warning("Audio processed, but no speech segments were returned.")
                    
                    st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                status.update(label="❌ Critical Error", state="error")
                st.error(f"Execution Error: {str(e)}")
                
    # Cleanup (Clean up automatically after run)
    # Note: In production, you might want more robust cleanup
    if os.path.exists(temp_path) and not process_btn:
        # We don't delete immediately if processing, handled by rerun logic
        pass