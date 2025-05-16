"""
Card schemas.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CardBase(BaseModel):
    note_id: int
    front_content: str
    back_content: str

class CardCreate(CardBase):
    pass

class CardUpdate(BaseModel):
    note_id: Optional[int] = None
    front_content: Optional[str] = None
    back_content: Optional[str] = None
    due_at: Optional[datetime] = None
    interval: Optional[int] = None
    ease_factor: Optional[float] = None
    reps: Optional[int] = None

class CardPublic(CardBase):
    id: int
    due_at: datetime
    interval: int
    ease_factor: float
    reps: int
    created_at: datetime
    updated_at: datetime

    model_config = { "from_attributes": True }

class CardReview(BaseModel):
    card_id: int
    rating: int  # Typically 1-4 representing ease of recall
