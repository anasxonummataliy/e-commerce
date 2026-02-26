from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas import UserRegister
from app.database.models import User


auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/register")
async def register(user_in: UserRegister, db: AsyncSession = Depends(get_db)):
    new_user = User(**user_in.model_dump())
    db.add(new_user)
    await db.commit()
    return "User qo'shildi."
