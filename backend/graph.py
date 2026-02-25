from langgraph.graph import StateGraph, END
from backend.state import AgentState
from backend.nodes import transcribe_node, segment_logic_node

def build_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("transcriber", transcribe_node)
    workflow.add_node("formatter", segment_logic_node)
    workflow.set_entry_point("transcriber")
    workflow.add_edge("transcriber", "formatter")
    workflow.add_edge("formatter", END)
    return workflow.compile()

app_graph = build_graph()