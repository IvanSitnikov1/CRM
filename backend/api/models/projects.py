from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, Date, Boolean, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.configs.database import Base
if TYPE_CHECKING:
    from api.models.users import User

class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    descriptions: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[Date] = mapped_column(Date, default=func.now())
    priority: Mapped[str] = mapped_column(String(50))
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    author: Mapped['User'] = relationship('User', back_populates='owned_projects')
    participants: Mapped[list['User']] = relationship('User', back_populates='participating_projects')
    tasks: Mapped[list['Task']] = relationship('Task', back_populates='project')


class Task(Base):
    __tablename__ = 'tasks'

    name: Mapped[str] = mapped_column(String(50))
    descriptions: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status: Mapped[str] = mapped_column(String(50))
    acting_position_id: Mapped[int] = mapped_column(ForeignKey('positions.id'))
    executor_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    acting_position: Mapped['Position'] = relationship('Position')
    executor: Mapped['User'] = relationship('User', back_populates='assigned_tasks')
    author: Mapped['User'] = relationship('User', back_populates='created_tasks')
    project: Mapped['Project'] = relationship('Project', back_populates='tasks')


class Position(Base):
    __tablename__ = 'positions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
