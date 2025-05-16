"""
Application initialization script.
"""
import logging
import os
from pathlib import Path

import structlog

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

if __name__ == "__main__":
    logger.info("Starting application initialization")
    
    # Create required directories
    migrations_dir = Path("migrations/versions")
    migrations_dir.mkdir(parents=True, exist_ok=True)
    
    # Create database schema
    logger.info("Creating database schema")
    os.system("alembic revision --autogenerate -m 'Initial migration'")
    os.system("alembic upgrade head")
    
    # Create initial data
    logger.info("Creating initial data")
    os.system("python scripts/init_db.py")
    
    logger.info("Application initialization complete")
