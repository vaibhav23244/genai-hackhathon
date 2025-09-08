from pydantic import Field
from langgraph.graph.message import add_messages, AnyMessage
from typing import TypedDict, Annotated, List, NotRequired

class AgentState(TypedDict):
    user_prompt: str = Field(description="Original prompt given by the user")
    refined_prompt: NotRequired[str] = Field(description="Refined version of the user prompt")
    messages: NotRequired[Annotated[List[AnyMessage], add_messages]] = Field(
        description="Messages in the agent state"
    )
