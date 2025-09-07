from pydantic import Field
from schema.initial_validator import InitialValidator
from langgraph.graph.message import add_messages, AnyMessage
from typing import TypedDict, Annotated, List, NotRequired, Literal

class GraphState(TypedDict):
    doc_name: str = Field(description="Name of the document")
    doc_content: NotRequired[str] = Field(description="Content of the document")
    messages: NotRequired[Annotated[List[AnyMessage], add_messages]] = Field(description="List of messages in the graph state")
    is_doc_valid: NotRequired[Literal["valid", "invalid"]] = Field(description="Indicates if the document is valid or invalid")
    doc_category: NotRequired[Literal["contract", "will", "affidavit", "article"]] = Field(description="Category of the document")
    is_valid: NotRequired[InitialValidator]
    doc_summary: NotRequired[str] = Field(description="Generated summary of the document")