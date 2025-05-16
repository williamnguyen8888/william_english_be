"""
Main application module.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from william_english_be.api.v1.api import api_router
from william_english_be.core.config import settings


def create_application() -> FastAPI:
    """
    Create the FastAPI application.
    """
    application = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application


app = create_application()
