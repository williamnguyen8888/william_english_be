"""
User schema.
"""
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    Base user schema.
    """
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """
    User creation schema.
    """
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    """
    User update schema.
    """
    password: Optional[str] = None


class UserInDBBase(UserBase):
    """
    Base schema for users in DB.
    """
    id: Optional[int] = None

    class Config:
        """
        Pydantic configuration.
        """
        from_attributes = True


class User(UserInDBBase):
    """
    User schema for API responses.
    """
    pass


class UserInDB(UserInDBBase):
    """
    User schema with hashed password.
    """
    hashed_password: str
