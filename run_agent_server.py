from pprint import pprint as pp
import langgraph_sdk as lg

api_base_url = "http://localhost:8123"
lgc = lg.get_sync_client(url=api_base_url)

assistant = lgc.assistants.create(assistant_id="785c8cbd-42d8-4546-8a68-57bc0f5301ad", graph_id="ready_or_not", if_exists="do_nothing")
pp(assistant)

assistants = lgc.assistants.search()
pp(f"# assistants: {len(assistants)}")

thread = lgc.threads.create()
pp(thread)

reply = lgc.runs.create(thread_id=thread['thread_id'],
                        assistant_id=assistant['assistant_id'],
                        input={"graph_state" : "What a nice day."})
pp(reply)
