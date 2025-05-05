from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, Date, Boolean, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.configs.database import Base
if TYPE_CHECKING:
    from api.models.users import User

class Project(Base):
    """Модель таблицы проектов"""

    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    descriptions: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String(20), unique=True)
    created_at: Mapped[Date] = mapped_column(Date, default=func.now())
    priority_id: Mapped[str] = mapped_column(ForeignKey('priorities.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    author: Mapped['User'] = relationship('User', back_populates='owned_projects')
    participants: Mapped[list['User']] = relationship('User', back_populates='participating_projects')
    tasks: Mapped[list['Task']] = relationship('Task', back_populates='project')


class Task(Base):
    """Модель таблицы задач проектов"""

    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    descriptions: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status: Mapped[str] = mapped_column(String(50))
    priority_id: Mapped[str] = mapped_column(ForeignKey('priorities.id'))
    acting_position_id: Mapped[int] = mapped_column(ForeignKey('positions.id'))
    executor_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
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
