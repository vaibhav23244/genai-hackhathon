import random
from langchain_core.messages import AIMessage
from uploader.uploader_graph_state.uploader_graph_state import GraphState

def not_valid(_: GraphState):
    responses = [
        "I'm not sure I understood that. Could you rephrase?",
        "Hmm, that doesn’t look like something I can help with yet.",
        "Can you try asking me in a different way?",
        "Sorry, I didn’t quite catch that. Want to reframe your request?",
        "That doesn’t seem like a valid input. Try something else!",
        "Oops, I can’t process that. Maybe ask me to summarize, explain, or do an action?",
        "Let’s try again — I think I missed your intent.",
    ]
    
    return {
        "messages": [AIMessage(content=random.choice(responses))]
    }
