from api.configs.app import app

from api.auth.routers import user_router


app.include_router(user_router)
