from fastapi import APIRouter

course_router = APIRouter()


@course_router.get("/courses")
async def get_courses() -> list[dict]:
    return []


@course_router.get("/courses/{course_id}")
async def get_course_by_id(course_id: int):
    pass


@course_router.post("/courses")
async def create_course(course_data):
    pass


@course_router.put("courses/{course_id}")
async def update_course(course_id: int):
    pass


@course_router.delete("courses/{course_id}")
async def delete_course(course_id: int):
    pass
