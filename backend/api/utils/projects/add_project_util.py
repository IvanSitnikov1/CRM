from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import connection
from api.schemas.projects import SProjectAdd
from api.models.projects import Project


@connection
async def add_project_util(project_data: SProjectAdd, session: AsyncSession):
    project = Project(**project_data.model_dump())
    session.add(project)
    await session.commit()
    return {'success'}
