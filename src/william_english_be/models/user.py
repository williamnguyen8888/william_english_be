"""
User model.
"""
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from william_english_be.db.base import Base


class User(Base):
    """
    User model.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
