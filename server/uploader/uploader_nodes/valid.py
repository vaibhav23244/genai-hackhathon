from llm import llm
from uploader.uploader_graph_state.uploader_graph_state import GraphState
# from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate

def valid(state: GraphState):
    messages = state['messages']
    last_message = messages[-1].content
    
    prompt = PromptTemplate(
        template='''You are a helpful assistant.
        Your task is to answer the user's question.
        The user's question is: {question}
        ''',
        input_variables=['question']
    )
    
    chain = prompt | llm
    response = chain.invoke({'question': last_message})
    return {
        "messages": response
    }
