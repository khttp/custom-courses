from fastapi import APIRouter

user_router = APIRouter()


@user_router.post("/register")
async def register():
    pass


@user_router.post("/login")
async def login():
    pass
