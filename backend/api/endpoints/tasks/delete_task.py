from fastapi import Depends

from api.configs.get_obj_db import get_task_repo
from api.db.task_repository import TaskDatabaseRepository


async def delete_task(
    task_id: int,
    tasks_repo: TaskDatabaseRepository = Depends(get_task_repo),
):
    await tasks_repo.delete(task_id)
    return
