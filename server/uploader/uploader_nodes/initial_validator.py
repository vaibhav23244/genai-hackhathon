from config.llm import llm
from langchain_core.prompts import PromptTemplate
from schema.initial_validator_schema import InitialValidatorSchema
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def initial_validator(state: GraphState):
    doc_content = state["doc_content"]
    prompt = PromptTemplate(
    template="""
        You are a binary classifier.

        Constraints:
        - Respond with only one word: either "true" or "false".
        - Use lowercase only, no punctuation, no explanation, no extra words.

        Task:
        - Read the document content below.
        - Determine if it is a legal document belonging to exactly one of these categories:
          1. Loan Agreement
          2. Rental Agreement
          3. Terms of Service
        - Respond "true" if it clearly belongs to one of these categories.
        - Respond "false" if it belongs to anything else (court orders, wills, affidavits, notices, personal text, circulars, articles, etc.).

        Document Content:
        {doc_content}
    """,
    input_variables=["doc_content"],
    )
    llm_with_structured_output = llm.with_structured_output(InitialValidatorSchema)
    chain = prompt | llm_with_structured_output
    response = chain.invoke({'doc_content': doc_content})
    return {'is_valid': response.is_valid}
