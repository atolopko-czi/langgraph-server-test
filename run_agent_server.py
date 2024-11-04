from pprint import pprint as pp
import langgraph_sdk as lg

api_base_url = "http://localhost:8123"
lgc = lg.get_sync_client(url=api_base_url)

assistant = lgc.assistants.create(name="Dynamic Graph 1",
                                  graph_id="graph_factory", 
                                  assistant_id="08c1160f-cb40-40f4-a13f-b62ebfb6538a",
                                  if_exists="do_nothing")
pp(assistant)

assistants = lgc.assistants.search()
pp(f"# assistants: {len(assistants)}")

thread = lgc.threads.create()
pp(thread)

reply = lgc.runs.wait(thread_id=thread['thread_id'],
                      assistant_id=assistant['assistant_id'],
                      config={"dyn_graph_key":"ready_or_not"},
                      input={"graph_state" : "What a nice day."})
pp(reply)
