from llm import llm
from langchain_core.prompts import ChatPromptTemplate
from agent.agent_graph_state.agent_graph_state import AgentState

def refine_prompt(state: AgentState):
    user_prompt = state["user_prompt"]

    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a helpful assistant that improves user prompts.\n"
         "Task: Rewrite the user's input into a **clear, professional, and effective prompt** "
         "that maximizes understanding and results.\n"
         "Rules:\n"
         "- Keep the intent of the prompt unchanged.\n"
         "- Make it easy to understand for an AI.\n"
         "- Make it concise but expressive.\n"
         "- If the user prompt is vague, add context to make it meaningful.\n"
         "- Ensure it's in natural, fluent English."),
        ("user", "{user_prompt}")
    ])

    chain = prompt | llm
    response = chain.invoke({"user_prompt": user_prompt})

    return {"refined_prompt": response}
