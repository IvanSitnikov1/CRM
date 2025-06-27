from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from api.DTO.endpoints.projects.read_project import ProjectReadResponseDTO, ProjectForResponseDTO
from api.DTO.endpoints.projects.update_project import ProjectUpdateDTO
from api.configs.get_obj_db import get_project_repo
from api.db.project_repository import ProjectDatabaseRepository


async def update_project(
    project_id: int,
    updated_data: ProjectUpdateDTO,
    project_repo: ProjectDatabaseRepository = Depends(get_project_repo),
):
    stmt = (select(project_repo.model_class).where(project_repo.model_class.id == project_id)
            .options(selectinload(project_repo.model_class.tasks)))
    updated_project = await project_repo.update(project_id, updated_data, stmt)
    return ProjectReadResponseDTO(
        detail='Проект изменен успешно',
        data=ProjectForResponseDTO.model_validate(updated_project),
    )
