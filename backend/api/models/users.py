from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.configs.database import Base
if TYPE_CHECKING:
    from api.models.projects import Project, Task


class ProjectParticipant(Base):
    """Модель для связи участников с проектами"""
    __tablename__ = 'project_participants'

    project_id: Mapped[int] = mapped_column(Integer, ForeignKey('projects.id'), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), primary_key=True)


class User(SQLAlchemyBaseUserTable, Base):
    """Модель таблицы пользователей"""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))

    photo: Mapped[str] = mapped_column(String(255), nullable=True)
    position: Mapped[str] = mapped_column(String(100), nullable=True)
    company: Mapped[str] = mapped_column(String(100), nullable=True)
    birthday_date: Mapped[Date] = mapped_column(Date, nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True) # подумать...
    phone_number: Mapped[str] = mapped_column(String(100), nullable=True)
    skype: Mapped[str] = mapped_column(String(100), nullable=True) # подумать...

    # Проекты, созданные пользователем
    owned_projects: Mapped[list['Project']] = relationship(
        'Project',
        back_populates='author',
        foreign_keys='Project.author_id'
    )

    # Удобный доступ к проектам участия
    participating_projects: Mapped[list['Project']] = relationship(
        'Project',
        secondary='project_participants',
        back_populates='participants',
        viewonly=True  # Только для чтения, изменения через ProjectParticipant
    )

    # Задачи
    created_tasks: Mapped[list['Task']] = relationship(
        'Task',
        back_populates='author',
        foreign_keys='Task.author_id',
    )

    assigned_tasks: Mapped[list['Task']] = relationship(
        'Task',
        back_populates='executor',
        foreign_keys='Task.executor_id',
    )
