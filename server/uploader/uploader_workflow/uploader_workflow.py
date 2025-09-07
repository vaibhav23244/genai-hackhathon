from langgraph.graph import START, StateGraph, END
from helpers.doc_validator_router import valid_router
from uploader.uploader_nodes.not_valid import not_valid
from uploader.uploader_nodes.summarizer import summarizer
from uploader.uploader_nodes.extract_content import extract_content
from uploader.uploader_nodes.doc_categorizer import doc_categorizer
from uploader.uploader_nodes.initial_validator import initial_validator
from uploader.uploader_graph_state.uploader_graph_state import GraphState
from uploader.uploader_nodes.explanation import explanation


uploader_workflow = StateGraph(GraphState)

uploader_workflow.add_node("not_valid", not_valid)
uploader_workflow.add_node("summarizer", summarizer) 
uploader_workflow.add_node("doc_categorizer", doc_categorizer)
uploader_workflow.add_node("extract_content", extract_content)
uploader_workflow.add_node("initial_validator", initial_validator)
uploader_workflow.add_node("explanation", explanation)

uploader_workflow.add_edge(START, "extract_content")
uploader_workflow.add_edge("extract_content", "initial_validator")
uploader_workflow.add_conditional_edges("initial_validator", valid_router, {
    "true": "doc_categorizer",
    "false": "not_valid",
})
uploader_workflow.add_edge("doc_categorizer", "summarizer")
uploader_workflow.add_edge("doc_categorizer","explanation")
uploader_workflow.add_edge("not_valid", END)    
uploader_workflow.add_edge("summarizer", END)