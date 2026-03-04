from builtins import str
from enum import Enum
from pydantic import BaseModel, EmailStr


class AuthProvider(str, Enum):
    local = "local"
    google = "google"


class UserCreate(BaseModel):
    email: EmailStr  # type: ignore
    username: str
    password: str
    full_name: str | None = None


class UserUpdate(BaseModel):
    username: str | None = None
    full_name: str | None = None
    avatar_url: str | None = None


class UserResponse(BaseModel):
    id: int
    email: EmailStr  # type: ignore
    username: str
    full_name: str | None
    avatar_url: str | None
    is_active: bool
    is_admin: bool
    auth_provider: AuthProvider

    model_config = {"from_attributes": True}
