import uuid
from datetime import date
from pydantic import BaseModel, validator, confloat
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship


class CourseType(Enum):
    Free = "public"
    Paid = "private"


class Category(SQLModel):
    id: uuid.UUID
    name: str
    course_id: uuid.UUID


class Contents(BaseModel):
    id: uuid.UUID
    name: str
    content_type: str
    duration: float


class CourseBase(SQLModel):
    name: str
    course_type: CourseType
    time_stamps: date
    rate: confloat(ge=0.0, le=10)
    content: list[Contents] = []


class CourseCreate(CourseBase):
    @validator("course_type", pre=True)
    def title_case_type(cls, value):
        return value.title()


class CourseWithID(CourseBase):
    id: uuid.UUID
