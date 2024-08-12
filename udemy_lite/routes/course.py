from fastapi import APIRouter
from ..models.course import CourseType, CourseBase, CourseCreate, CourseWithID

course_router = APIRouter()


@course_router.get("/courses")
async def get_courses() -> list[dict]:
    return []


@course_router.get("/courses/{course_id}")
async def get_course_by_id(course_id: int) -> CourseWithID:
    pass


@course_router.post("/courses")
async def create_course(course_data: CourseCreate) -> CourseWithID:
    pass


@course_router.put("courses/{course_id}")
async def update_course(course_id: int):
    pass


@course_router.delete("courses/{course_id}")
async def delete_course(course_id: int):
    pass
