from llm import llm
from langchain_core.prompts import PromptTemplate
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def summarizer(state: GraphState):
    doc_content = state["doc_content"]

    prompt = PromptTemplate(
        template='''
            You are a professional legal document summarizer.
        
            Task:
                - Read the document carefully.
                - First, provide a **brief 1–2 line overview** in plain English that anyone can understand.
                - Then, provide **5–7 detailed bullet points** covering all important aspects.  
                - Use clear, simple language.
                - The summary should look like a proper summary: first an intro, then structured bullets.
                - Do not omit critical legal details.
        
            Document Content:
            {doc_content}
        
            Summary:
        ''',
        input_variables=["doc_content"],
    )

    chain = prompt | llm
    response = chain.invoke({'doc_content': doc_content})

    return {"doc_summary": response}
