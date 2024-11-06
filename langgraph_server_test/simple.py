from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    graph_state: str

# Nodes
def node_1(state):
    print("---Node 1---")
    return {"graph_state":state['graph_state'] +"Version 3"}

# Build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)

builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

# Compile graph
graph = builder.compile()