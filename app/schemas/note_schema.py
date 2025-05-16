"""
Note schemas.
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None
    deck_id: int

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    deck_id: Optional[int] = None

class NotePublic(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = { "from_attributes": True }
