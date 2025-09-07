from llm import llm
from langchain_core.prompts import PromptTemplate
from schema.category_schema import CategorySchema
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def doc_categorizer(state: GraphState):
    doc_content = state['doc_content']
    template = PromptTemplate(
    template="""
        You are a document classifier.

        Task:
        - Read the document content provided.
        - Classify it into exactly one of the following categories:
          1. "Loan Agreement"
          2. "Rental Agreement"
          3. "Terms of Service"

        Constraints:
        - Respond with only one label, exactly as written above.
        - Do not include punctuation, explanation, or extra words.
        - Always use lowercase.

        Document Content:
        {doc_content}
    """,
    input_variables=["doc_content"],
    )
    llm_with_structured_output = llm.with_structured_output(CategorySchema)
    chain = template | llm_with_structured_output
    response = chain.invoke({'doc_content': doc_content})
    return {'doc_category': response.doc_category}