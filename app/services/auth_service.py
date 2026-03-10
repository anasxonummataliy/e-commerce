from builtins import str
from fastapi import Depends
from typing import Annotated

from app.repo.user_repo import UserRepo
from app.schemas.auth import Token
from app.core.security import create_access_token, create_refresh_token, hash_password
from app.schemas.user import UserCreate


class AuthService:
    def __init__(self, user_repo: Annotated[UserRepo, Depends()]):
        self.user_repo = user_repo

    async def register_user(self, user_in: UserCreate):
        data = user_in.model_dump()
        data["hashed_password"] = hash_password(data.pop("password"))
        new_user = await self.user_repo.create(**data)
        return Token(
            access_token=create_access_token({"sub": str(new_user.id)}),
            refresh_token=create_refresh_token({"sub": str(new_user.id)}),
        )
