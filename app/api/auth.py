from typing import Annotated
from fastapi import APIRouter, Depends, Query

from app.services.auth_service import AuthService
from app.schemas.user import UserCreate

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

AuthServiceDep = Annotated[AuthService, Depends()]


@auth_router.post("/register")
async def register(
        user_in: UserCreate, auth_service: AuthServiceDep
):
    return  await auth_service.register_user(user_in)


@auth_router.get("/login")
async def login():
    """Kirish endpointi"""
    return {"message": "Login endpoint - ishlayapti"}
