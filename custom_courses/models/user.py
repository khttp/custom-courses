from typing import Optional
import uuid
from sqlmodel import Relationship, SQLModel, Field

from custom_courses.models.course import Course


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    password: str
    courses: list[Course] = Relationship(back_populates="user")
