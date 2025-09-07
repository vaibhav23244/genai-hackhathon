from typing import Literal
from pydantic import BaseModel, Field

class CategorySchema(BaseModel):
    doc_category: Literal["Loan Agreement", "Rental Agreement", "Terms of Service"] = Field(description="Indicates if the initial validation passed or failed.")