from uploader.uploader_nodes.valid import valid
from uploader.uploader_nodes.not_valid import not_valid
from langgraph.graph import START, StateGraph, END
from uploader.uploader_nodes.valid_router import valid_router
from uploader.uploader_nodes.extract_content import extract_content
from uploader.uploader_nodes.initial_validator import initial_validator
from uploader.uploader_graph_state.uploader_graph_state import GraphState
from uploader.uploader_nodes.summarizer import summarizer

uploader_workflow = StateGraph(GraphState)

uploader_workflow.add_node("extract_content", extract_content)
uploader_workflow.add_node("initial_validator", initial_validator)
uploader_workflow.add_node("not_valid", not_valid)
uploader_workflow.add_node("valid", valid)
uploader_workflow.add_node("summarizer", summarizer) 

uploader_workflow.add_edge(START, "extract_content")
uploader_workflow.add_edge("extract_content", "initial_validator")
uploader_workflow.add_edge("initial_validator", END)
uploader_workflow.add_edge("initial_validator", "summarizer")
uploader_workflow.add_edge("summarizer", END)