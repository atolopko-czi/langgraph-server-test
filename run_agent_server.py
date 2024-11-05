from pprint import pprint as pp
import langgraph_sdk as lg

lgc1 = lg.get_sync_client(url="http://localhost:8001")
lgc2 = lg.get_sync_client(url="http://localhost:8002")

assistant1 = lgc1.assistants.create(name="Dynamic Graph 1",
                                  graph_id="graph_factory", 
                                  config={"dyn_graph_key":"ready_or_not"},
                                  )
pp(assistant1)

assistant2 = lgc2.assistants.update(assistant_id=assistant1['assistant_id'],
                                  graph_id="graph_factory", 
                                  config={"dyn_graph_key":"simple"},
                                  )

pp(assistant2)

# versions = lgc.assistants.get_versions(assistant_id=assistant1['assistant_id'])
# print(versions)

# assistants = lgc.assistants.search()
# pp(f"# assistants: {len(assistants)}")

# thread = lgc.threads.create()
# pp(thread)

reply = lgc1.runs.wait(thread_id=None,#thread['thread_id'],
                      assistant_id=assistant1['assistant_id'],
                      config={"dyn_graph_key":"simple"},
                      input={"graph_state" : "What a nice day."},
                      on_completion="delete")
pp(reply)

reply = lgc2.runs.wait(thread_id=None, #thread['thread_id'],
                      assistant_id=assistant2['assistant_id'],
                      config={"dyn_graph_key":"simple"},
                      input={"graph_state" : "What a nice day."},
                      on_completion="delete")
pp(reply)

