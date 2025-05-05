from fastapi import APIRouter


task_router = APIRouter(prefix="/api/v1/tasks", tags=["Задачи"])
