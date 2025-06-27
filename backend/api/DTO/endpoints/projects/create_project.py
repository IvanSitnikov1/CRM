from datetime import date

from pydantic import BaseModel, Field, ConfigDict


class ProjectCreateDTO(BaseModel):
    name: str
    descriptions: str | None = Field(None)
    number: str
    end_date: date
    priority_id: int = Field(1)
    author_id: int


class ProjectCreateResponseDTO(ProjectCreateDTO):
    id: int

    model_config = ConfigDict(from_attributes=True)

class ProjectCreateReadResponseDTO(BaseModel):
    detail: str
    data: ProjectCreateResponseDTO
