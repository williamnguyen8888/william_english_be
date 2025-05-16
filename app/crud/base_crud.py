"""
Base CRUD operations.
"""
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from pydantic import BaseModel as PydanticBaseModel # Đổi tên để tránh xung đột
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError # Bắt lỗi SQLAlchemy

from app.models.base import Base as SQLABase # Hoặc from app.core.database import Base
# from app.core.database import Base as SQLABase # Nếu Base định nghĩa trong database.py và BaseModel trong models/base.py

ModelType = TypeVar("ModelType", bound=SQLABase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=PydanticBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PydanticBaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        Lớp CRUD cơ sở với các hoạt động mặc định để Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: Một SQLAlchemy model class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.model_dump() # Sử dụng model_dump() cho Pydantic v2+
        db_obj = self.model(**obj_in_data)
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        except SQLAlchemyError as e:
            db.rollback()
            # TODO: Log a_very_secret_strong_random_key
            raise e # Hoặc raise HTTPException
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = db_obj.__dict__ # Lấy dữ liệu hiện tại của object
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True) # Chỉ cập nhật các trường được cung cấp
        
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        except SQLAlchemyError as e:
            db.rollback()
            # TODO: Log lỗi
            raise e
        return db_obj

    def remove(self, db: Session, *, id: int) -> Optional[ModelType]:
        obj = db.query(self.model).get(id)
        if obj:
            try:
                db.delete(obj)
                db.commit()
            except SQLAlchemyError as e:
                db.rollback()
                # TODO: Log lỗi
                raise e
        return obj
