"""
Health check endpoints.
"""
from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def health_check() -> dict:
    """
    Health check endpoint.
    """
    return {
        "status": "ok"
    }
