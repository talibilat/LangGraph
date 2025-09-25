#  Importing the libraries
from langgraph.graph import StateGraph
from typing import TypedDict, List



#  Defining the state
class AgentState(TypedDict):
    messages: List[str]


#  Defining the nodes
def greet(state: AgentState) -> AgentState:
    state["messages"] =  "Hey," + state["messages"] + '! How is your day going?'
    return state


#  Defining the graph
graph = StateGraph(AgentState)
graph.add_node("greeter", greet)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")


#  Compiling the graph
app = graph.compile()

#  Invoking the graph
result = app.invoke({"messages": "Bob"})
print("Result:", result)
print("Messages:", result["messages"])