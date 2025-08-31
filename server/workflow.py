from nodes.valid import valid
from graph_state import GraphState
from nodes.not_valid import not_valid
from nodes.valid_router import valid_router
from langgraph.graph import START, StateGraph, END
from nodes.initial_validator import initial_validator

workflow = workflow = StateGraph(GraphState)

workflow.add_node("initial_validator", initial_validator)
workflow.add_node("not_valid", not_valid)
workflow.add_node("valid", valid)

workflow.add_edge(START, "initial_validator")
workflow.add_conditional_edges("initial_validator", valid_router, {
    "true": "valid",
    "false": "not_valid"
})
workflow.add_edge("valid", END)
workflow.add_edge("not_valid", END)
