from datetime import datetime, timedelta, timezone
from typing import Any, Optional
import hashlib
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import JWT_SECRET, JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

#Password hasing context
#bycrypt is a strong hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _normalize_password(password: str) -> bytes:
    return hashlib.sha256(password.encode('utf-8')).digest()


def hash_password(password: str) -> str:
    """Hash a plaintext password."""
    normalized = _normalize_password(password)
    return pwd_context.hash(normalized)

def verify_password(plain_password: str, password_hash):
    "check if plaintext passwoord matches a stored hash"
    normalized = _normalize_password(plain_password)
    return pwd_context.verify(normalized, password_hash)

def create_access_token(*, sub: str, role: str, expires_minutes: Optional[int] = None) -> str:
    """Create a JWT access token.
    sub = 'subject' (who the token is about)
    role = teacher/student
    exp = expiry timestamp """

    if expires_minutes is None:
        expires_minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=expires_minutes)

    payload: dict[str, Any] = {
        "sub": sub,
        "role": role,
        "iat": now,
        "exp": expire,
    }

    return jwt.encode(payload, JWT_SECRET , algorithm=JWT_ALGORITHM)

def decode_token(token: str) -> dict[str, Any]:
    """Verify signature and expiry and return the payload"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError as e:
        raise ValueError("Invalid token") from e
