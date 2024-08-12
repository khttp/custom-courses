import uuid
from datetime import date, datetime, timedelta
from pydantic import BaseModel, confloat, validator
from enum import Enum
from typing import Literal


class Departments(Enum):
    ARTS_AND_HUMANITIESl = "Arts and Humanities"
    LIFE_SCIENCES = "Life Sciences"
    SCIENCE_AND_ENGINEERING = "Science and Engineering"


class Modules(BaseModel):
    id: int | uuid.UUID
    name: str
    professor: str
    credits: Literal[10, 20]
    registration_code: str


class STUDENT(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: confloat(ge=0, le=4)  # type: ignore
    course: str | None
    department: Departments
    fees_paid: bool
    modules: list[Modules] = []

    @validator("modules")
    def confirm_modules_of_size_3_if_exist(cls, value):
        if len(value) and len(value) != 3:
            raise ValueError("modules must be of size 3 or 0")
        return value

    @validator("date_of_birth")
    def ensure_over_18(cls, value):
        date_befor_18_yrs = datetime.now() - timedelta(days=365 * 18)
        date_befor_18_yrs = date_befor_18_yrs.date()
        if value > date_befor_18_yrs:
            raise ValueError("too young")
        return value
