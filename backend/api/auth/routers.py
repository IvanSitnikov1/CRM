from fastapi_users import FastAPIUsers

from api.models.users import User
from api.auth.users import auth_backend, get_user_manager
from api.routers.user_router import user_router
from api.schemas.users import SUserRead, SUserCreate, SUserUpdate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# Роут для логина (JWT)
user_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
)

# Роут для регистрации
user_router.include_router(
    fastapi_users.get_register_router(SUserRead, SUserCreate),
    prefix="",
)

# Роут для получения и изменения пользователей
user_router.include_router(
    fastapi_users.get_users_router(SUserRead, SUserUpdate),
    prefix="/users",
)
