"""
User model.
"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey # Thêm ForeignKey nếu cần
from sqlalchemy.orm import relationship
from .base import BaseModel # Hoặc from .base import Base

class User(BaseModel): # Kế thừa từ BaseModel (hoặc Base)
    __tablename__ = "users"

    # id, created_at, updated_at đã có từ BaseModel (nếu dùng)
    # Nếu không dùng BaseModel có sẵn các cột đó, hãy định nghĩa chúng ở đây:
    # id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    full_name = Column(String(255), index=True, nullable=True) # Ví dụ thêm trường

    # Ví dụ relationship: một User có nhiều Decks
    decks = relationship("Deck", back_populates="owner")
    review_logs = relationship("ReviewLog", back_populates="user") # Ví dụ
