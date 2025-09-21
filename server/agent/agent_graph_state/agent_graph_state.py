from pydantic import Field
from langchain_core.documents import Document
from typing import TypedDict, Annotated, List, NotRequired
from langgraph.graph.message import add_messages, AnyMessage

class AgentState(TypedDict):
    doc_name: str = Field(description="Name of the document")
    messages: Annotated[List[AnyMessage], add_messages] = Field(description="Messages in the agent state")
