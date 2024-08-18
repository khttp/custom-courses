from typing import Optional
import uuid
from sqlmodel import Relationship, SQLModel, Field

from udemy_lite.models.course import Course


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    password: str
    courses: list[Course] = Relationship(back_populates="user")
    enrollments: list["Enrolment"] = Relationship(back_populates="user")


class Enrolment(SQLModel, table=True):
    user_id: uuid.UUID = Field(foreign_key="user.id", primary_key=True)
    course_id: uuid.UUID = Field(foreign_key="course.id", primary_key=True)
    user: Optional["User"] = Relationship(back_populates="enrollments")
    course: Optional["Course"] = Relationship(back_populates="enrollments")
