from api.configs.app import app

from api.auth.routers import user_router
from api.router_factory import RouterFactory
from api.routes.project_routes import PROJECTS_ROUTES
from api.routes.task_routes import TASK_ROUTES


app.include_router(user_router)

project_router = RouterFactory(prefix='/api/v1/projects', tags=['Проекты'], routes=PROJECTS_ROUTES)
app.include_router(project_router())

task_router = RouterFactory(prefix='/api/v1/tasks', tags=['Задачи'], routes=TASK_ROUTES)
app.include_router(task_router())
