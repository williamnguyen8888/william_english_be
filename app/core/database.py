"""
Database configuration and session management.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base # declarative_base thay cho DeclarativeMeta
from app.core.config import settings

# Sử dụng create_engine cho kết nối đồng bộ với mysqlclient
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Nếu bạn quyết định dùng aiomysql và thao tác bất đồng bộ hoàn toàn:
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# engine = create_async_engine(settings.DATABASE_URL_ASYNC) # Cần DATABASE_URL_ASYNC trong settings
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency cho kết nối đồng bộ
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency cho kết nối bất đồng bộ (nếu dùng aiomysql)
# async def get_async_db():
#     async with SessionLocal() as session:
#         yield session
