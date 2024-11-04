import langgraph_server_test.ready_or_not as agent

print(agent.graph.invoke({"graph_state" : "What a nice day!"}))