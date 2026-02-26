from typing import TypeVar, Generic, Any
from sqlalchemy import Sequence, select
from sqlalchemy.engine.create import Type

from app.database.session import AsyncSession
from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class User(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
