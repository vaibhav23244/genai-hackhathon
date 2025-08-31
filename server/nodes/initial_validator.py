from llm import llm
from graph_state import GraphState
from schema.initial_validator import InitialValidator
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def initial_validator(state: GraphState):
    messages = state['messages']
    last_message = messages[-1].content
    
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content = """
                You are a binary classifier.

                Task:
                - Determine if the user's query is about understanding, simplifying, or explaining legal documents.
                - Respond with exactly one word:
                  - "true" → if query relates to legal documents, contracts, compliance, clauses, risks, or making them easier to understand.
                  - "false" → if unrelated.

                Constraints:
                - Do NOT add punctuation, explanation, or extra words.
                - Answer must be strictly "true" or "false".

                Examples:
                User: "Can you simplify this contract for me?"
                Assistant: true

                User: "What is a force majeure clause?"
                Assistant: true

                User: "Translate this agreement into plain English."
                Assistant: true

                User: "Tell me a joke."
                Assistant: false

                User: "Summarize today's cricket match."
                Assistant: false

                User: "What are my obligations under this NDA?"
                Assistant: true
                """
            ),
            MessagesPlaceholder(variable_name="messages"),
            HumanMessage(content=last_message),
        ]
    )

    llm_with_structured_output = llm.with_structured_output(InitialValidator)
    chain = prompt | llm_with_structured_output
    response = chain.invoke({'messages': messages})
    return {'is_valid': response.is_valid}
