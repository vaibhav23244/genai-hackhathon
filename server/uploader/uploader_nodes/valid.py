import random
from llm import llm
from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def valid(_: GraphState):
    responses = [
        "Got it! Let me process that for you.",
        "Thanks, I’ll take care of this request.",
        "Perfect — I can help with that.",
        "Alright, let’s move forward with your input.",
        "Great! I understand what you’re asking.",
        "Sounds good, let me handle this step.",
        "Okay, I know what to do here. Working on it!",
    ]
    
    return {
        "messages": [AIMessage(content=random.choice(responses))]
    }
