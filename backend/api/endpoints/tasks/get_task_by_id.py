from fastapi import Depends

from api.DTO.endpoints.tasks.read_task import TaskForResponseDTO, TaskReadResponseDTO
from api.configs.get_obj_db import get_task_repo
from api.db.task_repository import TaskDatabaseRepository


async def get_task_by_id(
    task_id: int,
    tasks_repo: TaskDatabaseRepository = Depends(get_task_repo),
):
    task = await tasks_repo.read_by_id(task_id)
    return TaskReadResponseDTO(
        detail='Задача получена успешно',
        data=TaskForResponseDTO.model_validate(task),
    )
