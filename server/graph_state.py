from pydantic import BaseModel, Field
from schema.initial_validator import InitialValidator
from typing import TypedDict, Annotated, List, NotRequired
from langgraph.graph.message import add_messages, AnyMessage

class GraphState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages] = Field(description="List of messages in the graph state")
    is_valid: NotRequired[InitialValidator]