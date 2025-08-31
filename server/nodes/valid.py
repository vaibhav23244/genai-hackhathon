import random
from graph_state import GraphState
from langchain_core.messages import AIMessage

def valid(_: GraphState):
    responses = [
        "Got it! Let’s continue 🚀",
        "Perfect, I can work with that.",
        "Nice, let’s move forward.",
        "Thanks, that makes sense.",
        "Awesome, let me process this.",
        "Cool, I’ll take it from here.",
        "Sounds good, let’s do this!",
    ]
    
    return {
        "messages": [AIMessage(content=random.choice(responses))]
    }
