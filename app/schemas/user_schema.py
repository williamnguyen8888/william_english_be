"""
User schemas.
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime # Để dùng cho created_at, updated_at

# Schema cơ sở cho các thuộc tính chung của User
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

# Schema cho việc tạo User (kế thừa từ UserBase, thêm password)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8) # Ví dụ yêu cầu password tối thiểu 8 ký tự

# Schema cho việc cập nhật User (tất cả các trường đều optional)
class UserUpdate(BaseModel): # Không kế thừa UserBase để cho phép cập nhật email riêng lẻ
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8)
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

# Schema cho User trả về từ DB (không bao gồm password hash)
class UserPublic(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    model_config = { "from_attributes": True } # Cho phép Pydantic đọc từ ORM model

# Schema cho User chứa trong DB (bao gồm cả password hash, dùng nội bộ)
class UserInDB(UserPublic): # Kế thừa UserPublic để có các trường public
    hashed_password: str
