from fastapi import Depends
from sqlalchemy.util.typing import Annotated
from app.repo.user_repo import UserRepo
from app.api.auth import TokenResponse, UserRegister


class AuthService:
    def __init__(self, user_repo: Annotated[UserRepo, Depends()]):
        self.user_repo = user_repo

    async def register_user(self, user_in: UserRegister):
        new_user = await self.user_repo.create(**user_in.model_dump())
        return TokenResponse(
            access_token="fake-token-for-user-" + str(new_user.id),
        )
