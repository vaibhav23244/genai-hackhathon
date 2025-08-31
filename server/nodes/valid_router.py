from graph_state import GraphState

def valid_router(state: GraphState):
    is_valid = state['is_valid']
    if is_valid == "true":
        return "true"
    else:
        return "false"