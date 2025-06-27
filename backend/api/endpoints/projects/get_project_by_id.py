from fastapi import Depends
from sqlalchemy.orm import selectinload

from api.DTO.endpoints.projects.read_project import ProjectReadResponseDTO, ProjectForResponseDTO
from api.configs.get_obj_db import get_project_repo
from api.db.project_repository import ProjectDatabaseRepository


async def get_project_by_id(
    project_id: int,
    project_repo: ProjectDatabaseRepository = Depends(get_project_repo),
):
    options = [selectinload(project_repo.model_class.tasks)]
    project = await project_repo.read_by_id(instance_id=project_id, options=options)
    return ProjectReadResponseDTO(
        detail='Проект получен успешно',
        data=ProjectForResponseDTO.model_validate(project),
    )
