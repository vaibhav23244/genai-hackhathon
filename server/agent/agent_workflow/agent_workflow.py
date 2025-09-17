from langgraph.graph import START, StateGraph, END
from agent.agent_nodes.refiner import refine_prompt
from agent.agent_nodes.rag_node import rag_pipeline
from agent.agent_nodes.extract_content import extract_content
from agent.agent_graph_state.agent_graph_state import AgentState

agent_workflow = StateGraph(AgentState)

# Add nodes
agent_workflow.add_node("refine_prompt", refine_prompt)
agent_workflow.add_node("extract_content", extract_content)
agent_workflow.add_node("rag_pipeline", rag_pipeline)

# Define edges
agent_workflow.add_edge(START, "rag_pipeline")
# agent_workflow.add_edge(START, "extract_content")
# agent_workflow.add_edge("extract_content", "refine_prompt")
agent_workflow.add_edge("rag_pipeline", END)
