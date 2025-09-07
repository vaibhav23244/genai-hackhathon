from llm import llm
from langchain_core.prompts import PromptTemplate
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def explanation(state: GraphState):
    doc_content = state["doc_content"]

    prompt = PromptTemplate(
        template='''
            You are a simple teacher who explains legal documents in a way that even a **10-year-old child can understand**.

            Task:
            - Read the document carefully.
            - Explain what it means in very **simple, everyday words**.
            - Start with a short 2–3 line explanation like:
              "This paper is about... It is usually used when..."
            - Then, give a few **easy-to-understand points** (like a story or bullet points) covering the important parts.
            - Do NOT use legal jargon (e.g., say "promise to pay back money" instead of "obligation to repay debt").
            - Keep it friendly and crystal clear for anyone, no matter their age or background.

            Document Content:
            {doc_content}
        ''',
        input_variables=["doc_content"],
    )

    chain = prompt | llm
    response = chain.invoke({"doc_content": doc_content})

    return {"doc_explanation": response}
