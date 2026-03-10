from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum as PyEnum
from sqlalchemy import Enum as SAEnum

from app.database.base import TimeBaseModel


class AuthProvider(PyEnum):
    local = "local"
    google = "google"


class User(TimeBaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, unique=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    auth_provider: Mapped[AuthProvider] = mapped_column(
        SAEnum(AuthProvider), default=AuthProvider.local
    )
    google_id: Mapped[str | None] = mapped_column(String, nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String, nullable=True)
