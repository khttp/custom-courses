from typing import Optional
import uuid
from datetime import date
from pydantic import field_validator, confloat
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel, create_engine


class CourseType(Enum):
    Free = "public"
    Paid = "private"


class Category(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    name: str
    courses: list["Course"] = Relationship(back_populates="courses")


class Content(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    name: str
    description: Optional["str"]
    content_type: str
    course_id: uuid.UUID = Field(foreign_key="course.id")
    course: "Course" = Relationship(back_populates="content")


class Course(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    name: str
    description: Optional["str"]
    course_type: CourseType
    time_stamps: date
    rate: confloat(ge=0.0, le=10)  # type: ignore
    user_id: uuid.UUID = Field(foreign_key="user.id")
    category_id: uuid.UUID = Field(foreign_key="category.id")
    content: list[Content] = Relationship(back_populates="course")
    user: Optional["User"] = Relationship(back_populates="courses")  # type: ignore
    category: Optional["Category"] = Relationship(back_populates="courses")  # type: ignore
    enrolments: list["Enrolment"] = Relationship(back_populates="course")  # type: ignore

    @field_validator("course_type")
    def title_case_type(cls, value):
        return value.title()


# Create an SQLite database engine
sqlite_file_name = "rf.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
