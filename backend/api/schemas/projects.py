from datetime import date

from pydantic import BaseModel, Field


class SProjectAdd(BaseModel):
    name: str
    descriptions: str | None = Field(None)
    number: str
    created_at: date
    priority_id: int
    author_id: int
