from pydantic import BaseModel, EmailStr, Field, field_validator
from .config import (
    MIN_USERNAME_LENGTH as user_min_len,
    MAX_USERNAME_LENGTH as user_max_len,
    MIN_PASSWORD_LENGTH as pass_min_len,
    MAX_PASSWORD_LENGTH as pass_max_len,
)


class UserBase(BaseModel):
    email: EmailStr
    username: str
    is_superuser: bool = Field(False)


class UserCreate(UserBase):
    email: EmailStr
    username: str
    password: str

    @field_validator("username")
    def validate_username_length(cls, value):
        if len(value) < int(user_min_len) or len(value) > int(user_max_len):
            raise ValueError("Username must be between 5 and 15 characters")

        return value
    
    @field_validator("password")
    def validate_password_complexity(cls, value):
        if len(value) < int(pass_min_len) or len(value) > int(pass_max_len):
            raise ValueError("Password must be between 5 and 30 characters")

        return value


class UserUpdate(UserBase):
    email: EmailStr | None
    username: str | None
    password: str | None


class User(UserBase):
    id: str

    class Config:
        from_attributes = True


class UserCreateDB(UserBase):
    id: str
    hashed_password: str | None
    