from nodes.valid import valid
from graph_state import GraphState
from nodes.not_valid import not_valid
from nodes.valid_router import valid_router
from langgraph.graph import START, StateGraph, END
from nodes.initial_validator import initial_validator
from nodes.doc_content_extractor import doc_content_extractor

workflow = workflow = StateGraph(GraphState)

workflow.add_node("doc_content_extractor", doc_content_extractor)
workflow.add_node("initial_validator", initial_validator)
workflow.add_node("not_valid", not_valid)
workflow.add_node("valid", valid)

workflow.add_edge(START, "doc_content_extractor")
workflow.add_edge("doc_content_extractor", END)
