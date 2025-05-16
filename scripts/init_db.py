"""
Create initial superuser.
"""
import logging
import sys
from pathlib import Path

import click
import structlog
from sqlalchemy.orm import Session

sys.path.append(str(Path(__file__).resolve().parent.parent))

from william_english_be.core.config import settings
from william_english_be.core.security import get_password_hash
from william_english_be.db.base import SessionLocal
from william_english_be.models.user import User

# Configure logging
logging.basicConfig(level=logging.INFO)
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


def init() -> None:
    """
    Initialize the database with a superuser.
    """
    db = SessionLocal()
    try:
        create_superuser(db)
    finally:
        db.close()


def create_superuser(db: Session) -> None:
    """
    Create a superuser in the database.
    """
    user = db.query(User).filter(User.email == "admin@example.com").first()
    if not user:
        logger.info("Creating admin superuser")
        user = User(
            email="admin@example.com",
            full_name="Admin",
            hashed_password=get_password_hash("admin"),
            is_superuser=True,
            is_active=True,
        )
        db.add(user)
        db.commit()
        logger.info("Superuser created", email="admin@example.com")
    else:
        logger.info("Superuser already exists", email="admin@example.com")


@click.command()
def main() -> None:
    """
    Run the initialization.
    """
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
