"""
Dependencies for API endpoints.
"""
from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session # Hoặc from sqlalchemy.ext.asyncio import AsyncSession nếu async

from app.core.database import get_db # Hoặc get_async_db
from app.core.security import oauth2_scheme, ALGORITHM # Lấy ALGORITHM từ security.py
from app.core.config import settings # Lấy SECRET_KEY từ settings
from app.schemas.token import TokenPayload
from app.models.user import User # Model User
from app.crud.crud_user import user_crud # Import crud_user

# Dependency để lấy DB session (đồng bộ)
def get_db_session() -> Generator[Session, None, None]:
    yield from get_db() # get_db là một generator

# Dependency để lấy DB session (bất đồng bộ) - nếu dùng
# async def get_async_db_session() -> AsyncGenerator[AsyncSession, None]:
#     async for session in get_async_db():
#         yield session


# Hàm này sẽ được hoàn thiện với logic query DB thực tế
async def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db_session) # Hoặc get_async_db_session
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenPayload(sub=username)
    except JWTError:
        raise credentials_exception
    
    # Bằng dòng này (giả sử 'sub' trong token là email của user):
    user = user_crud.get_by_email(db, email=token_data.sub)
    # Hoặc nếu 'sub' là user_id:
    # user = user_crud.get(db, id=int(token_data.sub))

    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user

async def get_current_active_superuser(
    current_user: User = Depends(get_current_active_user)
) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, # 403 Forbidden
            detail="The user doesn't have enough privileges"
        )
    return current_user
