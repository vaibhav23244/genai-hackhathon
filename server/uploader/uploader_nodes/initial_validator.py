from llm import llm
from langchain_core.prompts import PromptTemplate
from schema.initial_validator import InitialValidator
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def initial_validator(state: GraphState):
    doc_content = state["doc_content"]
    prompt = PromptTemplate(
        template='''
            You are a binary classifier.
            
            Task:
                - Read the document content provided.
                - Determine if it is a legal document belonging to one of these categories only:
                  1. Loan Agreement
                  2. Rental Agreement
                  3. Terms of Service

                - Respond with exactly one word:
                  - "true" → if it clearly belongs to one of these categories.
                  - "false" → if it belongs to ANYTHING else (court orders, wills, affidavits, notices, personal text, circulars, articles, etc.).

            Constraints:
                - Do NOT add punctuation, explanation, or extra words.
                - Answer must be strictly "true" or "false".

            Document Content:
            {doc_content}     
        ''',
        input_variables=["doc_content"],
    )
    llm_with_structured_output = llm.with_structured_output(InitialValidator)
    chain = prompt | llm_with_structured_output
    response = chain.invoke({'doc_content': doc_content})
    return {'is_valid': response.is_valid}
