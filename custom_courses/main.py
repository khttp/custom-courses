from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
import uvicorn
from custom_courses.auth import get_current_user
from custom_courses.routes.course import course_router
from custom_courses.routes.user import user_router
from .database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(course_router, dependencies=[Depends(get_current_user)])


def main_app():
    uvicorn.run("custom_courses.main:app", host="127.0.0.1", port=8000, reload=True)
