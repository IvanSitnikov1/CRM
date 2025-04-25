from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.configs.database import Base
if TYPE_CHECKING:
    from api.models.projects import Project, Task

class User(SQLAlchemyBaseUserTable, Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))

    photo: Mapped[str] = mapped_column(String(255))
    position: Mapped[str] = mapped_column(String(100), nullable=True)
    company: Mapped[str] = mapped_column(String(100), nullable=True)
    birthday_date: Mapped[Date] = mapped_column(Date, nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True) # подумать...
    phone_number: Mapped[str] = mapped_column(String(100), nullable=True)
    skype: Mapped[str] = mapped_column(String(100), nullable=True) # подумать...

    owned_projects: Mapped[list['Project']] = relationship('Project', back_populates='author')
    participating_projects: Mapped[list['Project']] = relationship('Project', back_populates='participants')
    created_tasks: Mapped[list['Task']] = relationship('Task', back_populates='author')
    assigned_tasks: Mapped[list['Task']] = relationship('Task', back_populates='executor')
