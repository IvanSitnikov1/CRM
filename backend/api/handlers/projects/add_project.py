from api.routers.project_router import project_router
from api.schemas.projects import SProjectAdd
from api.utils.projects.add_project_util import add_project_util


@project_router.post(
    '/add_project'
)
async def add_project(project_data: SProjectAdd):
    return await add_project_util(project_data)
