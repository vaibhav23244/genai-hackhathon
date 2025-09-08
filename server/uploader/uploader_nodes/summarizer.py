from config.llm import llm
from langchain_core.prompts import PromptTemplate
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def summarizer(state: GraphState):
    doc_content = state.get("doc_content", [])
    full_content = "\n".join([doc.page_content for doc in doc_content])
    if not full_content:
        return {"doc_summary": ""} 
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
            {full_content}
        
        ''',
        input_variables=["full_content"],
    )
    chain = prompt | llm
    response = chain.invoke({'full_content': full_content})
    return {"doc_summary": response}
