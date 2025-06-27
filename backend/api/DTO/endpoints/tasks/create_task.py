from pydantic import BaseModel, Field


class TaskCreateDTO(BaseModel):
    name: str
    descriptions: str | None = None
    planned_duration: int = Field(0)
    priority_id: int = Field(1)
    executor_id: int | None = None
    author_id: int
    project_id: int
