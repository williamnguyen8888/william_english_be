"""
Test configuration module.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from william_english_be.db.base import Base
from william_english_be.api.deps import get_db
from william_english_be.main import app


# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """
    Get a testing database session.
    """
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Connect to the database
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    # Begin a nested transaction
    nested = connection.begin_nested()
    
    # Yield the session for the test
    yield session
    
    # Rollback the nested transaction when the test is done
    session.close()
    nested.rollback()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db):
    """
    Get a TestClient instance with overridden dependencies.
    """
    # Override the get_db dependency
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    
    # Return the test client
    with TestClient(app) as test_client:
        yield test_client
    
    # Clear the overrides
    app.dependency_overrides = {}
