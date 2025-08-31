from llm import llm
from graph_state import GraphState
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
                - Determine if the user's query is about **understanding, simplifying, or explaining legal documents**.
                - Respond with exactly one word:
                  - "Valid" → if query relates to legal documents, contracts, compliance, clauses, risks, or making them easier to understand.
                  - "Not Valid" → if unrelated.

                Constraints:
                - Do NOT add punctuation, explanation, or extra words.
                - Answer must be strictly "Valid" or "Not Valid".

                Examples:
                User: "Can you simplify this contract for me?"
                Assistant: Valid

                User: "What is a force majeure clause?"
                Assistant: Valid

                User: "Translate this agreement into plain English."
                Assistant: Valid

                User: "Tell me a joke."
                Assistant: Not Valid

                User: "Summarize today's cricket match."
                Assistant: Not Valid

                User: "What are my obligations under this NDA?"
                Assistant: Valid
                """
            ),
            MessagesPlaceholder(variable_name="messages"),
            HumanMessage(content=last_message),
        ]
    )

    chain = prompt | llm
    response = chain.invoke({'messages': messages})
    return {'messages': [AIMessage(content=response.content)]}
