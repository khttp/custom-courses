from typing import Optional
import uuid
from datetime import date
from pydantic import field_validator, confloat
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel, create_engine


class CourseType(str, Enum):
    Public = "public"
    Private = "private"


class Category(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    courses: Optional[list["Course"]] = Relationship(back_populates="category")


class Content(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    description: Optional["str"]
    content_type: str
    course_id: uuid.UUID = Field(foreign_key="course.id")
    course: Optional["Course"] = Relationship(back_populates="content")


class Course(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    description: Optional["str"]
    course_type: CourseType
    time_stamps: date
    rate: confloat(ge=0.0, le=10)  # type: ignore
    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    category_id: uuid.UUID = Field(
        default_factory=uuid.uuid4, foreign_key="category.id"
    )
    content: list[Content] = Relationship(back_populates="course")
    user: "User" = Relationship(back_populates="courses")  # type: ignore
    category: "Category" = Relationship(back_populates="courses")  # type: ignore
    enrollments: list["Enrolment"] = Relationship(back_populates="course")  # type: ignore
