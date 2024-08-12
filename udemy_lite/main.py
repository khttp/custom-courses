from fastapi import FastAPI
from udemy_lite.routes.course import course_router
from udemy_lite.routes.user import user_router
import uvicorn

app = FastAPI()

app.include_router(course_router)
app.include_router(user_router)


def main_app():
    uvicorn.run("udemy_lite.main:app", host="127.0.0.1", port=8000, reload=True)
