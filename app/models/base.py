"""
Base model class.
"""
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from app.core.database import Base # Import Base từ database.py

class BaseModel(Base):
    __abstract__ = True # Đánh dấu đây là lớp trừu tượng, không tạo bảng trong DB

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

# Hoặc nếu không muốn BaseModel có sẵn id, created_at, updated_at,
# thì chỉ cần export Base:
# from app.core.database import Base
# class_registry = {} # Nếu dùng cách kế thừa từ Base = declarative_base(class_registry=class_registry)
