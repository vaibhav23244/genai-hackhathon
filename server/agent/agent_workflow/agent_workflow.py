from langgraph.graph import START, StateGraph, END
from agent.agent_nodes.rag_node import rag_pipeline
from agent.agent_graph_state.agent_graph_state import AgentState

agent_workflow = StateGraph(AgentState)

agent_workflow.add_node("rag_pipeline", rag_pipeline)

agent_workflow.add_edge(START, "rag_pipeline")
agent_workflow.add_edge("rag_pipeline", END)
