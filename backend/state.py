from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    audio_path: str
    raw_response: Dict[str, Any]
    script_segments: List[Dict[str, Any]]
    status: str