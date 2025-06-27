from api.db.base_database_repository import BaseDatabaseRepository
from api.models.projects import Task


class TaskDatabaseRepository(BaseDatabaseRepository):
    """Репозиторий для работы с базой данных задач."""
    model_class = Task
