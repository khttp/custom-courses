from contextlib import asynccontextmanager
from fastapi import FastAPI
from udemy_lite.routes.course import course_router
from udemy_lite.routes.user import user_router
from .database import create_db_and_tables
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(course_router)
app.include_router(user_router)


def main_app():
    uvicorn.run("udemy_lite.main:app", host="127.0.0.1", port=8000, reload=True)
