from fastapi import FastAPI, HTTPException
from udemy_lite.schema import CourseType, CourseBase, CourseCreate, CourseWithID

app = FastAPI()


courses = [
    {
        "id": 1,
        "name": "Python",
        "description": "Python course",
        "course_type": "free",
        "price": 0,
        "content": [
            {
                "id": 1,
                "name": "intro to python",
                "content_type": "video",
                "duration": 12.4,
            }
        ],
    },
    {
        "id": 2,
        "name": "Django",
        "description": "Django course",
        "course_type": "free",
        "price": 100,
    },
    {
        "id": 3,
        "name": "FastAPI",
        "description": "FastAPI course",
        "course_type": "paid",
        "price": 200,
    },
]


@app.get("/courses")
def get_courses(
    course_type: CourseType | None = None, has_contents: bool = False
) -> list[CourseWithID]:
    course_list = [CourseWithID(**course) for course in courses]
    if course_type:
        return [course for course in course_list if course.course_type == course_type]
    if has_contents:
        return [course for course in course_list if len(course.content) > 0]
    return course_list


@app.get("/courses/{course_id}")
def get_course_by_id(course_id: int) -> CourseWithID:
    course = next(
        (CourseWithID(**course) for course in courses if course["id"] == course_id),
        None,
    )
    if not course:
        raise HTTPException(404, "course not found")
    return course


@app.post("/courses")
async def create_course(course_data: CourseCreate) -> CourseWithID:
    id = len(courses)
    course = CourseWithID(id=id + 1, **course_data.model_dump()).model_dump()
    courses.append(course)
    print(courses)
    return course
