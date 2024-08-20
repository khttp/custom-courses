from datetime import datetime, date
from uuid import UUID
from .models.course import CourseType


def convert_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def convert_uuid(uuid_str: str) -> UUID:
    return UUID(uuid_str)


def convert_course_type(course_type_str: str) -> CourseType:
    return CourseType(course_type_str)
