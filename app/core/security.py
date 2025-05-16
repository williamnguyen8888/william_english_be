"""
Security utilities for authentication and authorization.
"""
from datetime import datetime, timedelta, timezone # Thêm timezone
from typing import Optional, Any, Union

from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.schemas.token import TokenPayload # Đảm bảo import đúng

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# URL để client lấy token, khớp với endpoint login của bạn
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"/api/v1/auth/login/access-token" # Sửa thành f-string hoặc settings.API_V1_STR + "/auth/login"
)

ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_MINUTES = settings.REFRESH_TOKEN_EXPIRE_MINUTES

def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM) # Có thể dùng SECRET_KEY khác cho refresh token
    return encoded_jwt
    
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Hàm get_current_user và get_current_active_user sẽ được hoàn thiện hơn
# khi có CRUD layer và được chuyển sang app/api/deps.py
# Đây là placeholder ban đầu để các phần khác có thể import.
# Việc query DB để lấy user thực tế sẽ nằm trong deps.py
async def get_current_user_placeholder():
    # Logic này sẽ được thay thế bằng logic thực tế trong deps.py
    raise NotImplementedError("get_current_user not implemented yet in security.py, use deps.py version")
