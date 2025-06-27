from fastapi import Depends

from api.DTO.endpoints.tasks.create_task import TaskCreateDTO
from api.DTO.endpoints.tasks.read_task import TaskReadResponseDTO, TaskForResponseDTO
from api.configs.get_obj_db import get_task_repo
from api.db.task_repository import TaskDatabaseRepository


async def create_task(
    task_data: TaskCreateDTO,
    task_repo: TaskDatabaseRepository = Depends(get_task_repo),
):
    new_task = await task_repo.create(task_data)
    return TaskReadResponseDTO(
        detail='Задача создана успешно',
        data=TaskForResponseDTO.model_validate(new_task),
    )
