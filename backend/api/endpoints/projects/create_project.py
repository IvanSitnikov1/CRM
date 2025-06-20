from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import get_async_session
from api.DTO.endpoints.projects.create_project import ProjectCreateDTO, ProjectCreateResponseDTO
from api.models.projects import Project


async def create_project(
        project_data: ProjectCreateDTO,
        session: AsyncSession = Depends(get_async_session),
):
    new_project = Project(**project_data.model_dump())
    session.add(new_project)
    await session.commit()
    await session.refresh(new_project)
    return new_project
    # return ProjectCreateResponseDTO(new_project)
