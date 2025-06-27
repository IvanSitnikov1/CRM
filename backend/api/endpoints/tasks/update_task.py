from fastapi import Depends

from api.DTO.endpoints.tasks.read_task import TaskReadResponseDTO, TaskForResponseDTO
from api.DTO.endpoints.tasks.update_task import TaskUpdateDTO
from api.configs.get_obj_db import get_task_repo
from api.db.task_repository import TaskDatabaseRepository


async def update_task(
    task_id: int,
    updated_data: TaskUpdateDTO,
    task_repo: TaskDatabaseRepository = Depends(get_task_repo),
):
    task = await task_repo.update(task_id, updated_data)
    return TaskReadResponseDTO(
        detail='Задача изменена успешно',
        data=TaskForResponseDTO.model_validate(task),
    )
