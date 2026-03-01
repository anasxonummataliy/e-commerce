from enum import Enum
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import TimeBaseModel


class AuthProvider(Enum):
    local = "local"
    google = "google"


class User(TimeBaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, unique=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str] = mapped_column(String)
    is_activeL: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    auth_provider: Mapped[AuthProvider] = mapped_column(
        Enum(AuthProvider), default=AuthProvider.local
    )
    google_id: Mapped[str | None] = mapped_column(String, nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String, nullable=True)
