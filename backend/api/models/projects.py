from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.models.users import User

from sqlalchemy import String, Integer, Date, Boolean, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from api.configs.database import Base


class Project(Base):
    """Модель таблицы проектов"""
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    descriptions: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String(20), unique=True)
    created_at: Mapped[Date] = mapped_column(Date, default=func.now())
    end_date: Mapped[Date] = mapped_column(Date)
    priority_id: Mapped[int] = mapped_column(ForeignKey('priorities.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # Автор проекта
    author: Mapped['User'] = relationship(
        'User',
        back_populates='owned_projects',
        foreign_keys=[author_id]
    )

    # Удобный доступ к участникам через association_proxy
    participants: Mapped[list['User']] = relationship(
        'User',
        secondary='project_participants',
        back_populates='participating_projects',
        viewonly=True  # Только для чтения, изменения через ProjectParticipant
    )

    tasks: Mapped[list['Task']] = relationship(
        'Task',
        back_populates='project',
        cascade='all, delete-orphan'
    )

    @hybrid_property
    def calculated_duration(self) -> int:
        return sum(task.actual_duration or 0 for task in self.tasks)


class Task(Base):
    """Модель таблицы задач проектов"""
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    descriptions: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_id: Mapped[int] = mapped_column(ForeignKey('status_tasks.id'), default=1)
    planned_duration: Mapped[int] = mapped_column(Integer)
    actual_duration: Mapped[int] = mapped_column(Integer, nullable=True)
    priority_id: Mapped[int] = mapped_column(ForeignKey('priorities.id'))
    executor_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'))

    executor: Mapped['User'] = relationship(
        'User',
        back_populates='assigned_tasks',
        foreign_keys=[executor_id],
    )
    author: Mapped['User'] = relationship(
        'User',
        back_populates='created_tasks',
        foreign_keys=[author_id],
    )
    project: Mapped['Project'] = relationship('Project', back_populates='tasks')


class Position(Base):
    """Модель таблицы существующих должностей"""
    __tablename__ = 'positions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))


class Priority(Base):
    """Модель таблицы приоритетов"""
    __tablename__ = 'priorities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))


class StatusTask(Base):
    """Модель таблицы статусов задач."""
    __tablename__ = 'status_tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
