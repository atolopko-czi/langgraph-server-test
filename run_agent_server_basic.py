import os
from pprint import pprint as pp
import langgraph_sdk as lg

lgc1 = lg.get_sync_client(url=os.getenv("LANGRAPH_API_BASE_URL", "http://localhost:8123"))
                          
assistant = lgc1.assistants.create(name="Dynamic Graph 1",
                                   graph_id="graph_factory", 
                                  )
pp(assistant)

reply = lgc1.runs.wait(thread_id=None,#thread['thread_id'],
                      assistant_id=assistant['assistant_id'],
                      config={"dyn_graph_key":"simple"},
                      input={"graph_state" : "What a nice day."},
                      on_completion="delete")
pp(reply)
