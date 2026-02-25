import os
import requests
import mimetypes
from backend.state import AgentState
from config.settings import config

def transcribe_node(state: AgentState) -> AgentState:
    headers = {"Authorization": f"Bearer {config.API_KEY}"}
    
    # Dynamically figure out if it's mp3, wav, m4a, etc.
    mime_type, _ = mimetypes.guess_type(state["audio_path"])
    mime_type = mime_type or "audio/mpeg" # Fallback
    
    try:
        with open(state["audio_path"], "rb") as f:
            files = {"file": (os.path.basename(state["audio_path"]), f, mime_type)}
            data = {
                "model": config.MODEL_NAME,
                "response_format": "verbose_json", 
                "timestamp_granularities[]": "segment"
            }
            
            # ADDED TIMEOUT: 120 seconds max. No more infinite hanging!
            response = requests.post(
                config.API_URL, 
                headers=headers, 
                files=files, 
                data=data,
                timeout=120 
            )
            
            if response.status_code != 200:
                return {"status": f"API Error ({response.status_code}): {response.text}"}
            return {"raw_response": response.json(), "status": "Success"}
            
    except requests.exceptions.Timeout:
        return {"status": "Error: The Qubrid API timed out after 2 minutes."}
    except Exception as e:
        return {"status": f"System Error: {str(e)}"}

def segment_logic_node(state: AgentState) -> AgentState:
    raw_data = state.get("raw_response", {})
    segments = raw_data.get("segments", [])
    
    if not segments:
        text = raw_data.get("text", "No speech detected.")
        return {"script_segments": [{"id": 0, "timestamp": "00:00", "speaker": "Speaker 1", "text": text}]}

    formatted = []
    for i, seg in enumerate(segments):
        m, s = divmod(int(seg.get("start", 0)), 60)
        formatted.append({
            "id": i,
            "timestamp": f"{m:02}:{s:02}",
            "speaker": "Speaker ?", 
            "text": seg.get("text", "").strip()
        })
    return {"script_segments": formatted}