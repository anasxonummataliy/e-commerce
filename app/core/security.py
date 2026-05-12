import jwt
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash

from app.core.config import settings

ph = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return ph.check(hashed, plain)


def create_access_token(data: dict) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        {**data, "exp": expire},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def create_refresh_token(data: dict) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )
    return jwt.encode(
        {**data, "exp": expire, "type": "refresh"},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )
