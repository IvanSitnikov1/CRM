from pydantic import ConfigDict, BaseModel

from api.DTO.endpoints.projects.create_project import ProjectCreateDTO
from api.DTO.endpoints.tasks.read_task import TaskForResponseDTO


class ProjectForResponseDTO(ProjectCreateDTO):
    id: int
    calculated_duration: int
    tasks: list[TaskForResponseDTO]

    model_config = ConfigDict(from_attributes=True)


class ProjectReadResponseDTO(BaseModel):
    detail: str
    data: ProjectForResponseDTO


class ProjectsListReadResponseDTO(BaseModel):
    detail: str
    data: list[ProjectForResponseDTO]
