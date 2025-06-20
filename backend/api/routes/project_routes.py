from fastapi import status

from api.DTO.endpoints.projects.create_project import ProjectCreateResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.projects.create_project import create_project

PROJECTS_ROUTES = [
    RouteDTO(
        path="/create_project",
        endpoint=create_project,
        response_model=ProjectCreateResponseDTO,
        methods=["POST"],
        status_code=201,
        summary="Создание проекта",
        description="",
        responses={
            status.HTTP_201_CREATED: {
                "description": "Проект создан успешно",
            },
            status.HTTP_400_BAD_REQUEST: {
                "description": "Некорректные данные в запросе",
                "content": {
                    "application/json": {
                        "example": {"detail": "Некорректные данные в запросе"}
                    }
                },
            },
        },
    ),
]
