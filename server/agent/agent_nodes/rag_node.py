from config.llm import llm
from helpers.retriever import get_retriever
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from agent.agent_graph_state.agent_graph_state import AgentState


def rag_pipeline(state: AgentState):
    user_prompt = state['messages'][-1].content
    doc_name = state["doc_name"]
    retriever = get_retriever(doc_name)
    docs = retriever.get_relevant_documents(user_prompt)
    context = "\n\n".join([doc.page_content for doc in docs]) if docs else "No relevant context found."
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer the user's question using the provided context."),
        ("system", "Context:\n{context}"),
        ("user", "{query}")
    ])
    chain = prompt | llm
    response = chain.invoke({"context": context, "query": user_prompt})
    return {"messages": [AIMessage(content=response.content)]}