from typing import TypeVar, Generic, Any
from sqlalchemy import Sequence, select
from sqlalchemy.engine.create import Type

from app.database.session import AsyncSession
from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(cls, db: AsyncSession, **kwargs) -> ModelType:
        obj = cls(**kwargs)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    async def get(self, db: AsyncSession, _id: Any) -> ModelType | None:
        result = await db.execute(select(self.model).filter_by(id=_id))
        return result.scalar_one_or_none()

    async def get_all(self, db: AsyncSession) -> Sequence[ModelType]:
        result = await db.execute(select(self.model))
        return result.scalars().all()

    async def update(self, db: AsyncSession, _id: Any, **kwargs) -> ModelType | None:
        obj = await self.get(db, _id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            await db.commit()
            await db.refresh(obj)
        return obj
