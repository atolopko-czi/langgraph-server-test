from langchain_core.runnables import RunnableConfig
from langgraph.graph.state import StateGraph

def make_graph(config: RunnableConfig) -> StateGraph:
    print(f"MAKING GRAPH with {config}")
    if config['dyn_graph_key'] == "simple":
        from langgraph_server_test.simple import graph
        return graph
    else:
        from langgraph_server_test.ready_or_not import graph
        return graph