import uuid
import base64

from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_hash_string(password: str) -> str:
    return pwd_context.hash(password)


def create_access_key() -> str:
    return base64.b64encode(uuid.uuid4().hex.encode("ascii"))


def create_access_secret() -> str:
    return base64.b64encode(
        f"{uuid.uuid4().hex}{uuid.uuid4().hex}".encode("ascii"))
