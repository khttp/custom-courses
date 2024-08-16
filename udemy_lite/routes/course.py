from fastapi import APIRouter, Depends, HTTPException
from ..models.course import Course, Category, Content
from sqlmodel import Session, select
from ..database import get_session
import uuid

course_router = APIRouter()


@course_router.get("/courses")
async def get_courses(session: Session = Depends(get_session)) -> list[Course]:
    courses = session.exec(select(Course)).all()
    return courses


@course_router.get("/courses/{course_id}")
async def get_course_by_id(
    course_id: uuid.UUID, session: Session = Depends(get_session)
) -> Course:
    course = session.get(Course, course_id)
    return course


@course_router.post("/courses")
async def create_course(
    course: Course, session: Session = Depends(get_session)
) -> Course:
    db_course = Course.model_validate(course)
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course


@course_router.put("courses/{course_id}")
async def update_course(
    course_id: uuid.UUID, NewCourse: Course, session: Session = Depends(get_session)
) -> Course:
    db_course = session.get(Course, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="page not found")
    course = NewCourse.model_dump(exclude_unset=True)
    for key, value in course.items:
        setattr(db_course, key, value)
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course


@course_router.delete("courses/{course_id}")
async def delete_course(
    course_id: uuid.UUID, session: Session = Depends(get_session)
) -> dict:
    db_course = Session.get(Course, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="page not found")
    session.delete(db_course)
    session.commit()
    return {"OK": True}
