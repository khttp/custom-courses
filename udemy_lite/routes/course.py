from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from ..models.course import Course, Category, Content
from sqlmodel import Session, select
from ..database import get_session
import uuid

course_router = APIRouter()


@course_router.get("/category")
async def get_category(session: Session = Depends(get_session)):
    categories = session.exec(select(Category)).all()
    return categories


@course_router.post("/category")
async def add_category(category: Category, session: Session = Depends(get_session)):
    category.id = uuid.UUID(category.id)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


@course_router.get("/category/{category_id}")
async def get_category_by_ID(
    category_id: uuid.UUID, session: Session = Depends(get_session)
):
    category = session.get(Category, category_id)
    return category


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
    course.id = uuid.UUID(course.id)
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course


@course_router.put("/courses/{course_id}")
async def update_course(
    course_id: uuid.UUID, NewCourse: Course, session: Session = Depends(get_session)
) -> Course:
    db_course = session.get(Course, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="page not found")
    course = NewCourse.model_dump(exclude_unset=True)
    for key, value in course.items():
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
async def get_contents(course_id: uuid.UUID, session: Session = Depends(get_session)):
    contents = session.exec(select(Content).where(course_id=course_id)).all()
    return contents


@course_router.post("/courses/{course_id}/contents")
async def create_contents(
    new_content: Content, session: Session = Depends(get_session)
):
    db_content = Course.model_validate(new_content)
    session.add(db_content)
    session.commit()
    session.refresh(db_content)
    return db_content


@course_router.get("/courses/{course_id}/{content_id}")
async def get_content_by_id(
    course_id: uuid.UUID, content_id, session: Session = Depends(get_session)
) -> Content:
    content = session.exec(
        select(Content).where(course_id == course_id and content_id == content_id)
    )
    return content


@course_router.put("/courses/{course_id}/{content_id}")
async def change_content(
    new_content: Content,
    content_id: uuid.UUID,
    course_id: uuid.UUID,
    session: Session = Depends(get_session),
):
    db_content = session.exec(
        select(Content).where(course_id == course_id and content_id == content_id)
    )
    if not db_content:
        raise HTTPException(status_code=404, detail="page not found")
    content = new_content.model_dump(exclude_unset=True)
    for key, value in content.items:
        setattr(db_content, key, value)
    session.add(db_content)
    session.commit()
    session.refresh(db_content)
    return db_content


@course_router.delete("/courses/{course_id}/{content_id}")
async def delete_content(
    course_id: uuid.UUID, content_id: uuid.UUID, session: Session = Depends(get_session)
):
    db_content = session.exec(
        select(Content).where(course_id == course_id and content_id == content_id)
    )
    if not db_content:
        raise HTTPException(status_code=404, detail="page not found")
    session.delete(db_content)
    session.commit()
    return {"OK": True}
