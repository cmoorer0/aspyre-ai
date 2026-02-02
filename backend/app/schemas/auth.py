from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    role: Literal["teacher", "student"]

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class MeResponse(BaseModel):
    id: int
    email: EmailStr
    role: Literal["teacher", "student"]