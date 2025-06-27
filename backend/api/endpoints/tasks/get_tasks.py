from fastapi import Depends

from api.DTO.endpoints.tasks.read_task import TaskForResponseDTO, TaskListReadResponseDTO
from api.configs.get_obj_db import get_task_repo
from api.db.task_repository import TaskDatabaseRepository


async def get_tasks(
    tasks_repo: TaskDatabaseRepository = Depends(get_task_repo),
):
    tasks = await tasks_repo.read_all()
    return TaskListReadResponseDTO(
        detail='Список задач получен успешно',
        data=[TaskForResponseDTO.model_validate(task) for task in tasks],
    )
