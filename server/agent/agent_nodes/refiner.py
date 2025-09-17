from config.llm import llm
from agent.agent_graph_state.agent_graph_state import AgentState
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def refine_prompt(state: AgentState):
    chat_history = state["messages"]
    doc_content = state["doc_content"]  
    print(doc_content)
    user_prompt = chat_history[-1].content
    prompt = ChatPromptTemplate.from_messages([
        ("system",'''
         You are a helpful assistant that rewrites and improves user prompts.\n
         Task: Rewrite the user's query into a **clear, professional, and effective prompt** 
         that maximizes understanding and results, while aligning it with the provided document content.\n
         \n
         Rules:\n
         - Preserve the original intent of the user query.\n
         - Refine the query so it is consistent with both the **document content** and the **chat history**.\n
         - Make the rewritten prompt concise, natural, and expressive.\n
         - If the query is vague, add missing context from the document to make it meaningful.\n
         - Ensure the final rewritten prompt is fluent and easy for an AI to understand.
         Here is the relevant document content:\n{doc_content}\n
        '''),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{user_prompt}")
    ])
    chain = prompt | llm
    response = chain.invoke({"user_prompt": user_prompt, "chat_history": chat_history, "doc_content": doc_content})
    return {"refined_prompt": response}
