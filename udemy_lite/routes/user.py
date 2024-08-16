from fastapi import APIRouter
from ..models.user import User

user_router = APIRouter()


@user_router.post("/register")
async def create_user(user: User) -> User:
    pass


@user_router.post("/login")
async def login(user: User) -> User:
    pass
