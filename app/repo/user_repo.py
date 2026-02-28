from typing import TypeVar, Generic, Any
from sqlalchemy import Sequence, select
from sqlalchemy.engine.create import Type

from app.database.models.user import User
from app.database.session import AsyncSession
from app.database.base import Base
from app.repo.base_repo import BaseRepository


class UserRepo(BaseRepository[User]):
    pass
