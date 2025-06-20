from api.configs.app import app

from api.auth.routers import user_router
from api.router_factory import RouterFactory
from api.routes.project_routes import PROJECTS_ROUTES


app.include_router(user_router)

project_router = RouterFactory(prefix='/projects', tags=['Проекты'], routes=PROJECTS_ROUTES)
app.include_router(project_router())
