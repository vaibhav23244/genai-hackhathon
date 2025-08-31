from pydantic import Field
from typing import Optional, TypedDict, Annotated, List
from langgraph.graph.message import add_messages, AnyMessage

class GraphState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages] = Field(description="List of messages in the graph state")