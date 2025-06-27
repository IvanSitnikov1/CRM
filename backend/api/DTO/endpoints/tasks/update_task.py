from pydantic import BaseModel, Field


class TaskUpdateDTO(BaseModel):
    name: str | None = Field(None)
    descriptions: str | None = Field(None)
    planned_duration: int | None = Field(None)
    actual_duration: int | None = Field(None)
    priority_id: int | None = Field(None)
    executor_id: int | None = Field(None)
    is_active: bool | None = Field(None)
    status_id: int | None = Field(None)
