from api.db.base_database_repository import BaseDatabaseRepository
from api.models.projects import Project


class ProjectDatabaseRepository(BaseDatabaseRepository):
    """Репозиторий для работы с базой данных проектов."""
    model_class = Project
