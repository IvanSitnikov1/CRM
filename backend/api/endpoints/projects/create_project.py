from fastapi import Depends

from api.configs.get_obj_db import get_project_repo
from api.DTO.endpoints.projects.create_project import (
    ProjectCreateDTO, ProjectCreateResponseDTO, ProjectCreateReadResponseDTO)
from api.db.project_repository import ProjectDatabaseRepository


async def create_project(
    project_data: ProjectCreateDTO,
    project_repo: ProjectDatabaseRepository = Depends(get_project_repo),
):
    new_project = await project_repo.create(project_data)
    return ProjectCreateReadResponseDTO(
        detail='Проект создан успешно',
        data=ProjectCreateResponseDTO.model_validate(new_project),
    )
