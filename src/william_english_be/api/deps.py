"""
Dependencies module for FastAPI.
"""
from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from william_english_be.core.config import settings
from william_english_be.db.base import SessionLocal
# from william_english_be.models.user import User
# from william_english_be.schemas.token import TokenPayload

# reusable_oauth2 = OAuth2PasswordBearer(
#     tokenUrl=f"{settings.API_V1_STR}/login/access-token"
# )


def get_db() -> Generator:
    """
    Get database session.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# def get_current_user(
#     db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
# ) -> User:
#     """
#     Get current user from token.
#     """
#     try:
#         payload = jwt.decode(
#             token, settings.SECRET_KEY, algorithms=["HS256"]
#         )
#         token_data = TokenPayload(**payload)
#     except (JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = db.query(User).filter(User.id == token_data.sub).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
