from typing import TypeVar, Generic, Any
from sqlalchemy import Sequence, select
from sqlalchemy.engine.create import Type

from app.database.base import Base
from app.router.depends import DBsession

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType], session: DBsession):
        self.model = model
        self.session = session

    async def create(self, **kwargs) -> ModelType:
        obj = self.model(**kwargs)
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def get(self, _id: Any) -> ModelType | None:
        result = await self.session.execute(select(self.model).filter_by(id=_id))
        return result.scalar_one_or_none()

    async def get_all(self) -> Sequence[ModelType]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def update(self, obj: ModelType, **kwargs) -> ModelType | None:
        for key, value in kwargs.items():
            setattr(obj, key, value)
        await self.session.commit()
        await self.session.refresh(obj)
