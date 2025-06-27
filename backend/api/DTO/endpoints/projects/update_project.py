from pydantic import BaseModel, Field


class ProjectUpdateDTO(BaseModel):
    name: str | None = Field(None)
    descriptions: str | None = Field(None)
    priority_id: int | None = Field(None)
