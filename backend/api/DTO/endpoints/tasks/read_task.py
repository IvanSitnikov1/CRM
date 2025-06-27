from pydantic import ConfigDict, BaseModel

from api.DTO.endpoints.tasks.create_task import TaskCreateDTO


class TaskForResponseDTO(TaskCreateDTO):
    id: int
    is_active: bool
    status_id: int
    actual_duration: int | None = None

    model_config = ConfigDict(from_attributes=True)


class TaskReadResponseDTO(BaseModel):
    detail: str
    data: TaskForResponseDTO


class TaskListReadResponseDTO(BaseModel):
    detail: str
    data: list[TaskForResponseDTO]
