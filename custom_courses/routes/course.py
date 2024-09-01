from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from ..models import Course, Content, User, CourseType
from sqlmodel import Session, select
from ..database import get_session
import uuid
from ..utils import convert_date, convert_uuid, convert_course_type

course_router = APIRouter()


# TODO
# categorize the courses to make the search for public courses easy
# @course_router.get("/category")
# async def get_category(session: Session = Depends(get_session)):
#     categories = session.exec(select(Category)).all()
#     return categories
#
#
# @course_router.post("/category")
# async def add_category(category: Category, session: Session = Depends(get_session)):
#     category.id = uuid.UUID(category.id)
#     session.add(category)
#     session.commit()
#     session.refresh(category)
#     return category
#
#
# @course_router.get("/category/{category_id}")
# async def get_category_by_ID(
#     category_id: uuid.UUID, session: Session = Depends(get_session)
# ):
#     category = session.get(Category, category_id)
#     return category
#
#
@course_router.get("/courses/public")
async def get_public_courses(session: Session = Depends(get_session)) -> list[Course]:
    statement = select(Course).where(Course.course_type == "public")
    public_courses = session.exec(statement).all()
    return public_courses


@course_router.get("/users/me/courses")
async def get_user_courses(
    current_user_id: uuid.UUID, session: Session = Depends(get_session)
) -> list[Course]:
    user = session.get(User, current_user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user.courses


@course_router.post("/users/me/courses")
async def add_user_course(
    user_id: uuid.UUID, new_course: Course, session: Session = Depends(get_session)
) -> Course:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    if new_course.rate < 0 or new_course.rate > 10:
        raise ValueError("rate must be from 0 and 10")
    new_course.user_id = user_id
    new_course.id = uuid.UUID(new_course.id)
    new_course.course_type = convert_course_type(new_course.course_type)
    session.add(new_course)
    session.commit()
    session.refresh(new_course)
    return new_course


@course_router.get("/courses/{course_id}")
async def get_course_by_id(
    course_id: uuid.UUID, session: Session = Depends(get_session)
) -> Course:
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    return course


@course_router.put("/courses/{course_id}")
async def update_course(
    course_id: uuid.UUID, NewCourse: dict, session: Session = Depends(get_session)
) -> Course:
    db_course = session.get(Course, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="page not found")
    if "time_stamps" in NewCourse:
        NewCourse["time_stamps"] = convert_date(NewCourse["time_stamps"])
    if "user_id" in NewCourse:
        NewCourse["user_id"] = convert_uuid(NewCourse["user_id"])
    if "category_id" in NewCourse:
        NewCourse["category_id"] = convert_uuid(NewCourse["category_id"])
    if "course_type" in NewCourse:
        NewCourse["course_type"] = convert_course_type(NewCourse["course_type"])
    if "rate" in NewCourse:
        if NewCourse["rate"] > 10 or NewCourse["rate"] < 0:
            raise ValueError("rate attribute must be value from 0 to 10")
    for key, value in NewCourse.items():
        setattr(db_course, key, value)
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course


@course_router.delete("/courses/{course_id}")
async def delete_course(
    course_id: uuid.UUID, session: Session = Depends(get_session)
) -> dict:
    db_course = session.get(Course, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="page not found")
    session.delete(db_course)
    session.commit()
    return {"OK": True}


@course_router.get("/courses/{course_id}/contents")
async def get_contents(course_id: str, session: Session = Depends(get_session)):
    course = session.get(Course, uuid.UUID(course_id))
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    return course.content


@course_router.post("/courses/{course_id}/contents")
async def create_contents(
    course_id: uuid.UUID, new_content: Content, session: Session = Depends(get_session)
):
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    new_content.course_id = course_id
    new_content.id = uuid.UUID(new_content.id)
    session.add(new_content)
    session.commit()
    session.refresh(new_content)
    return new_content


@course_router.get("/contents/{content_id}")
async def get_content_by_id(
    content_id: str, session: Session = Depends(get_session)
) -> Content:
    content = session.get(Content, uuid.UUID(content_id))
    if not content:
        raise HTTPException(status_code=404, detail="content not found")
    return content


@course_router.put("/contents/{content_id}")
async def change_content(
    new_content: dict,
    content_id: uuid.UUID,
    session: Session = Depends(get_session),
):
    db_content = session.get(Content, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="page not found")
    for key, value in new_content.items():
        setattr(db_content, key, value)
    session.add(db_content)
    session.commit()
    session.refresh(db_content)
    return db_content


@course_router.delete("/contents/{content_id}")
async def delete_content(
    content_id: uuid.UUID, session: Session = Depends(get_session)
):
    db_content = session.get(Content, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="page not found")
    session.delete(db_content)
    session.commit()
    return {"OK": True}
