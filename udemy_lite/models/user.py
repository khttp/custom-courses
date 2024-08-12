import uuid
from pydantic import BaseModel


class UserBase(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    password: str


class Enrolment(BaseModel):
    course_id: uuid.UUID
    user_id: uuid.UUID
