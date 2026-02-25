import os
import requests
from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- 1. Define the State ---
class AgentState(TypedDict):
    audio_path: str          # Path to the uploaded file
    raw_response: Dict       # Raw JSON from Whisper API
    script_segments: List    # Formatted list for the UI
    status: str              # Current status

# --- 2. Define the Nodes ---

def transcribe_node(state: AgentState):
    """Sends audio to the Qubrid Whisper API."""
    audio_path = state["audio_path"]
    api_key = os.getenv("QUBRID_API_KEY") 
    
    # UPDATED: Using the exact URL you provided
    api_url = "https://platform.qubrid.com/api/v1/qubridai/audio/transcribe"

    if not api_key:
        return {"status": "Error: Missing QUBRID_API_KEY in .env"}

    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        # Open the file from the path saved in state
        with open(audio_path, "rb") as f:
            # We explicitly name the file "audio.wav" or keep original filename
            files = {"file": (os.path.basename(audio_path), f, "audio/wav")}
            
            # UPDATED: We MUST add 'verbose_json' to get the timestamps
            data = {
                "model": "openai/whisper-large-v3",
                "response_format": "verbose_json", 
                "timestamp_granularities[]": "segment"
            }
            
            # Send request
            response = requests.post(api_url, headers=headers, files=files, data=data)
            
            if response.status_code != 200:
                return {"status": f"API Error {response.status_code}: {response.text}"}
            
            # Return the JSON response to the state
            return {"raw_response": response.json(), "status": "Transcribing Complete"}
            
    except Exception as e:
        return {"status": f"Error: {str(e)}"}

def segment_logic_node(state: AgentState):
    """
    Refines raw Whisper segments into a clean script format.
    """
    raw_data = state.get("raw_response", {})
    
    # Whisper usually returns 'segments' in verbose_json mode
    segments = raw_data.get("segments", [])
    
    # Fallback if the API returns just 'text' (no timestamps)
    if not segments and "text" in raw_data:
        return {
            "script_segments": [{
                "id": 0, 
                "timestamp": "00:00", 
                "speaker": "Speaker 1", 
                "text": raw_data["text"]
            }], 
            "status": "Warning: No timestamps found. Returned raw text."
        }

    formatted_script = []
    
    for i, seg in enumerate(segments):
        start_time = seg.get("start", 0)
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        timestamp = f"{minutes:02}:{seconds:02}"
        
        formatted_script.append({
            "id": i,
            "timestamp": timestamp,
            "speaker": "Speaker ?", # Placeholder for UI editing
            "text": seg.get("text", "").strip()
        })
        
    return {"script_segments": formatted_script, "status": "Formatting Complete"}

# --- 3. Build the Graph ---
workflow = StateGraph(AgentState)

workflow.add_node("transcriber", transcribe_node)
workflow.add_node("formatter", segment_logic_node)

workflow.set_entry_point("transcriber")

workflow.add_edge("transcriber", "formatter")
workflow.add_edge("formatter", END)

app_graph = workflow.compile()