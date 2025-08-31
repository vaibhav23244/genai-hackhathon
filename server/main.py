from graph_state import GraphState
from graph import initial_validator
from langgraph.graph import START, StateGraph, END

workflow = StateGraph(GraphState)

workflow.add_node("initial_validator", initial_validator)

workflow.add_edge(START, "initial_validator")
workflow.add_edge("initial_validator", END)

graph = workflow.compile()