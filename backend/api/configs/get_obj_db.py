from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import get_async_session
from api.db.project_repository import ProjectDatabaseRepository
from api.db.task_repository import TaskDatabaseRepository


async def get_project_repo(session: AsyncSession = Depends(get_async_session)):
    yield ProjectDatabaseRepository(session)


async def get_task_repo(session: AsyncSession = Depends(get_async_session)):
    yield TaskDatabaseRepository(session)
