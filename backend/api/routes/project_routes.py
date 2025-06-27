from fastapi import status

from api.DTO.endpoints.projects.create_project import ProjectCreateReadResponseDTO
from api.DTO.endpoints.projects.read_project import ProjectReadResponseDTO, \
    ProjectsListReadResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.projects.create_project import create_project
from api.endpoints.projects.delete_project import delete_project
from api.endpoints.projects.get_project_by_id import get_project_by_id
from api.endpoints.projects.get_projects import get_projects
from api.endpoints.projects.update_project import update_project

PROJECTS_ROUTES = [
    RouteDTO(
        path="/create",
        endpoint=create_project,
        response_model=ProjectCreateReadResponseDTO,
        methods=["POST"],
        status_code=201,
        summary="Создание проекта",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "Проект создан успешно",
            },
            status.HTTP_409_CONFLICT: {
                "description": "Нарушение уникальности при создании проекта",
                "content": {
                    "application/json": {
                        "example": {"detail": "Некорректные данные в запросе"}
                    }
                },
            },
        },
    ),
    RouteDTO(
        path="",
        endpoint=get_projects,
        response_model=ProjectsListReadResponseDTO,
        methods=["GET"],
        status_code=200,
        summary="Получение списка проектов",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "Список проектов получен успешно",
            },
        },
    ),
    RouteDTO(
        path="/{project_id}",
        endpoint=get_project_by_id,
        response_model=ProjectReadResponseDTO,
        methods=["GET"],
        status_code=200,
        summary="Получение проекта по id",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "Проект получен успешно",
            },
        },
    ),
    RouteDTO(
        path="/{project_id}",
        endpoint=update_project,
        response_model=ProjectReadResponseDTO,
        methods=["PATCH"],
        status_code=200,
        summary="Изменение проекта по id",
        description="",
        responses={
            status.HTTP_200_OK: {
                "description": "Проект изменен успешно",
            },
        },
    ),
    RouteDTO(
        path="/{project_id}",
        endpoint=delete_project,
        response_model=None,
        methods=["DELETE"],
        status_code=204,
        summary="Удаление проекта по id",
        description="",
        responses={
            status.HTTP_204_NO_CONTENT: {
                "description": "Проект удален успешно",
            },
        },
    ),
]
