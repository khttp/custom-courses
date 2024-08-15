from typing import Optional
import uuid
from sqlmodel import Relationship, SQLModel, Field

from udemy_lite.models.course import Course


class User(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    name: str
    email: str
    password: str
    courses: list[Course] = Relationship(back_populates="user")
    enrolments: list["Enrolment"] = Relationship(back_populates="user")


class Enrolment(SQLModel, table=True):
    user_id: Optional[uuid.UUID] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    course_id: Optional[int] = Field(
        default=None, foreign_key="course.id", primary_key=True
    )

    user: Optional["User"] = Relationship(back_populates="enrollments")
    course: Optional["Course"] = Relationship(back_populates="enrollments")
