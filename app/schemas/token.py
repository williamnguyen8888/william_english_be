"""
Token schemas for authentication.
"""
from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: Optional[str] = None # Tùy chọn nếu dùng refresh token

class TokenPayload(BaseModel):
    sub: Optional[str] = None # Subject (thường là user_id hoặc email)
    # exp: Optional[int] = None # Thời gian hết hạn (đã được xử lý bởi JWT)
