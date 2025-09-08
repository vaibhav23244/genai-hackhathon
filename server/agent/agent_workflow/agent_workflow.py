from langgraph.graph import START, StateGraph, END
from agent.agent_graph_state.agent_graph_state import AgentState
from agent.agent_nodes.refiner import refine_prompt

agent_workflow = StateGraph(AgentState)

# Add nodes
agent_workflow.add_node("refine_prompt", refine_prompt)

# Define edges
agent_workflow.add_edge(START, "refine_prompt")
agent_workflow.add_edge("refine_prompt", END)
