"""
CRUD operations for User model.
"""
from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session

from app.crud.base_crud import CRUDBase # Nếu dùng base_crud.py
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.core.security import get_password_hash # Để hash password

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        # Trước khi tạo, hash password
        hashed_password = get_password_hash(obj_in.password)
        # Tạo một dict từ Pydantic model, loại bỏ password gốc
        # và thêm hashed_password
        db_obj_data = obj_in.model_dump(exclude={"password"})
        db_obj = User(**db_obj_data, hashed_password=hashed_password)
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, 
        db: Session, 
        *, 
        db_obj: User, 
        obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        # Nếu password được cung cấp trong update_data, hash nó
        if "password" in update_data and update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            update_data["hashed_password"] = hashed_password
            del update_data["password"] # Xóa password gốc khỏi update_data
        
        # Gọi phương thức update của lớp cha (CRUDBase)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser

user_crud = CRUDUser(User) # Tạo một instance để sử dụng trong services
