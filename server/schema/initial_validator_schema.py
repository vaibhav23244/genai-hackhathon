from typing import Literal
from pydantic import BaseModel, Field

class InitialValidatorSchema(BaseModel):
    is_valid: Literal["true", "false"] = Field(description="Indicates if the initial validation passed or failed.")