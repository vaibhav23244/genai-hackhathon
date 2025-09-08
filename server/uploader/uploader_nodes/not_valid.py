from config.llm import llm
from langchain_core.prompts import PromptTemplate
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def not_valid(state: GraphState):
    doc_content = state['doc_content']
    template = PromptTemplate(
        template='''
        You are a document validation assistant.

        Task:
        - Review the provided document content.
        - If it is NOT one of the accepted categories below, explain clearly and concisely why it is being rejected.

        Accepted categories:
        1. Loan Agreement
        2. Rental Agreement
        3. Terms of Service

        Response requirements:
        - Output only a short rejection message (2–4 sentences).
        - State the main reason for rejection (e.g., "This looks like a court order, not a rental agreement").
        - Mention the closest matching document type if possible (e.g., "This resembles a legal notice").
        - Provide a short example of valid content for comparison.
        - Keep the explanation simple, avoid legal jargon.

        Document Content:
        {doc_content}
        ''',
        input_variables=['doc_content'],
    )
    chain = template | llm
    response = chain.invoke({'doc_content': doc_content})
    return {'doc_invalid_reason': response.content}