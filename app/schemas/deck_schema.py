"""
Deck schemas.
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
# from .tag_schema import TagPublic # Ví dụ nếu có TagSchema

class DeckBase(BaseModel):
    name: str
    description: Optional[str] = None

class DeckCreate(DeckBase):
    pass

class DeckUpdate(DeckBase):
    name: Optional[str] = None # Cho phép cập nhật từng phần

class DeckPublic(DeckBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    # tags: List[TagPublic] = [] # Ví dụ nếu muốn trả về tags

    model_config = { "from_attributes": True }
