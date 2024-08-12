from pydantic import BaseModel, validator
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship


class CourseType(Enum):
    Free = "free"
    Paid = "paid"


class Contents(BaseModel):
    id: int
    name: str
    content_type: str
    duration: float


class CourseBase(BaseModel):
    name: str
    description: str
    course_type: CourseType
    price: int
    content: list[Contents] = []


class CourseCreate(CourseBase):
    @validator("course_type", pre=True)
    def title_case_type(cls, value):
        return value.title()


class CourseWithID(CourseBase):
    id: int
