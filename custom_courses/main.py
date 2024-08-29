from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from custom_courses.auth import get_current_user
from custom_courses.routes.course import course_router
from custom_courses.routes.user import user_router
from .database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="custom-courses",  # Change this to your project name
    description="a website that allow users to create and share educational courses ,these courses are a collection of free structured organized contents books ,PDFs ,vids ,images ,summary ...",
    version="1.0.0",  # set the version of your project
    contact={
        "name": "Abdelrahman Khattab",
        "email": "abdelrahmankhattab9999@gmail.com",
    },
    license_info={
        "name": "mit license",
        "url": "https://opensource.org/licenses/mit",
    },
    openapi_tags=[{"name": "auth", "description": "Authentication"}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace "*" with your frontend url in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/auth", tags=["auth"])
app.include_router(
    course_router, tags=["courses"], dependencies=[Depends(get_current_user)]
)


def main_app():
    uvicorn.run("custom_courses.main:app", host="127.0.0.1", port=8000, reload=True)
