import os
import requests
from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from config import settings

class AgentState(TypedDict):
    audio_path: str
    raw_response: Dict
    script_segments: List
    status: str

def transcribe_node(state: AgentState):
    headers = {"Authorization": f"Bearer {settings.API_KEY}"}
    try:
        with open(state["audio_path"], "rb") as f:
            files = {"file": (os.path.basename(state["audio_path"]), f, "audio/wav")}
            data = {
                "model": settings.MODEL_NAME,
                "response_format": "verbose_json", 
                "timestamp_granularities[]": "segment"
            }
            response = requests.post(settings.API_URL, headers=headers, files=files, data=data)
            if response.status_code != 200:
                return {"status": f"Error: {response.text}"}
            return {"raw_response": response.json(), "status": "Success"}
    except Exception as e:
        return {"status": f"Error: {str(e)}"}

def segment_logic_node(state: AgentState):
    raw_data = state.get("raw_response", {})
    segments = raw_data.get("segments", [])
    
    # Critical: If no segments, try to parse the 'text' key as a single block
    if not segments:
        text = raw_data.get("text", "No transcription generated.")
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

workflow = StateGraph(AgentState)
workflow.add_node("transcriber", transcribe_node)
workflow.add_node("formatter", segment_logic_node)
workflow.set_entry_point("transcriber")
workflow.add_edge("transcriber", "formatter")
workflow.add_edge("formatter", END)
app_graph = workflow.compile()