from fastapi import Depends

from api.configs.get_obj_db import get_project_repo
from api.db.project_repository import ProjectDatabaseRepository


async def delete_project(
    project_id: int,
    project_repo: ProjectDatabaseRepository = Depends(get_project_repo),
):
    await project_repo.delete(project_id)
    return
