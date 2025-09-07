from pydantic import Field
from typing import TypedDict, NotRequired
from schema.category_schema import CategorySchema
from schema.initial_validator_schema import InitialValidatorSchema

class GraphState(TypedDict):
    doc_category: NotRequired[CategorySchema] 
    is_valid: NotRequired[InitialValidatorSchema]
    doc_name: str = Field(description="Name of the document")
    doc_content: NotRequired[str] = Field(description="Content of the document")
    doc_summary: NotRequired[str] = Field(description="Generated summary of the document")
    doc_invalid_reason: NotRequired[str] = Field(description="Reason why the document is invalid, if applicable")
    doc_explanation: NotRequired[str] = Field(description="Beginner-friendly explanation of the document")