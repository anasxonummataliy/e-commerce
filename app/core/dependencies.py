from fastapi import Depends
from typing import Annotated
from app.database.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession


DBsession = Annotated[AsyncSession, Depends(get_session)]
