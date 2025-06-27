from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from api.DTO.endpoints.projects.read_project import ProjectsListReadResponseDTO, \
    ProjectForResponseDTO
from api.configs.get_obj_db import get_project_repo
from api.db.project_repository import ProjectDatabaseRepository


async def get_projects(
    project_repo: ProjectDatabaseRepository = Depends(get_project_repo),
):
    stmt = select(project_repo.model_class).options(selectinload(project_repo.model_class.tasks))
    projects = await project_repo.read_all(stmt=stmt)
    return ProjectsListReadResponseDTO(
        detail='Список проектов получен успешно',
        data=[ProjectForResponseDTO.model_validate(project) for project in projects],
    )
