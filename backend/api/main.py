from api.configs.app import app

from api.auth.routers import user_router
from api.handlers import project_router


app.include_router(user_router)
app.include_router(project_router)
