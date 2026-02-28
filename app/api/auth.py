from typing import Annotated
from fastapi import APIRouter, Depends, Query

from app.schemas import UserRegister, QParams
from app.schemas.auth import TokenResponse
from app.services.auth_service import AuthService


auth_router = APIRouter(prefix="/auth", tags=["Auth"])

AuthServiceDep = Annotated[AuthService, Depends()]


@auth_router.post("/register")
async def register(
    user_in: UserRegister, auth_service: AuthServiceDep
) -> TokenResponse:
    """Ro'yxatdan o'tish endpointi"""
    return await auth_service.register_user(user_in)


@auth_router.get("")
async def login(params: Annotated[QParams, Query()]):
    """Kirish endpointi"""
    return {"message": "Login endpoint - ishlayapti"}
