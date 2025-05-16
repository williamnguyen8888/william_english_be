"""
API module for v1.
"""
from fastapi import APIRouter

from william_english_be.api.v1 import health

api_router = APIRouter()

# Include active routers
api_router.include_router(health.router, prefix="/health", tags=["health"])

# Import and include other routers as needed
# from william_english_be.api.v1 import users, login
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(login.router, prefix="/login", tags=["login"])
