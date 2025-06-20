from datetime import date

from pydantic import BaseModel, Field


class ProjectCreateDTO(BaseModel):
    name: str
    descriptions: str | None = Field(None)
    number: str
    end_date: date
    priority_id: int
    author_id: int


class ProjectCreateResponseDTO(ProjectCreateDTO):
    id: int
    sum_actual_duration: int
