from pydantic import BaseModel, EmailStr
from enum import Enum


class AuthProvider(str, Enum):
    local = "local"
    google = "google"


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: str | None = None


class UserUpdate(BaseModel):
    username: str | None = None
    full_name: str | None = None
    avatar_url: str | None = None


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    full_name: str | None
    avatar_url: str | None
    is_active: bool
    is_admin: bool
    auth_provider: AuthProvider

    model_config = {"from_attributes": True}
