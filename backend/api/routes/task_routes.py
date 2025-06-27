from fastapi import status

from api.DTO.endpoints.tasks.read_task import TaskReadResponseDTO, TaskListReadResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.tasks.delete_task import delete_task
from api.endpoints.tasks.get_task_by_id import get_task_by_id
from api.endpoints.tasks.create_task import create_task
from api.endpoints.tasks.get_tasks import get_tasks
from api.endpoints.tasks.update_task import update_task

TASK_ROUTES = [
    RouteDTO(
        path="/create",
        endpoint=create_task,
        response_model=TaskReadResponseDTO,
        methods=["POST"],
        status_code=201,
        summary="Создание задачи",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "Задача создана успешно",
            },
        },
    ),
    RouteDTO(
        path="",
        endpoint=get_tasks,
        response_model=TaskListReadResponseDTO,
        methods=["GET"],
        status_code=200,
        summary="Получение списка всех задач",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "Список задач получен успешно",
            },
        },
    ),
    RouteDTO(
        path="/{task_id}",
        endpoint=get_task_by_id,
        response_model=TaskReadResponseDTO,
        methods=["GET"],
        status_code=200,
        summary="Получение задачи по id",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "Задача получена успешно",
            },
        },
    ),
    RouteDTO(
        path="/{task_id}",
        endpoint=update_task,
        response_model=TaskReadResponseDTO,
        methods=["PATCH"],
        status_code=200,
        summary="Редактирование задачи",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "Задача создана изменена",
            },
        },
    ),
    RouteDTO(
        path="/{task_id}",
        endpoint=delete_task,
        response_model=None,
        methods=["DELETE"],
        status_code=204,
        summary="Удаление задачи по id",
        description="",
        responses={
            status.HTTP_204_NO_CONTENT: {
                "description": "Задача удалена успешно",
            },
        },
    ),
]
