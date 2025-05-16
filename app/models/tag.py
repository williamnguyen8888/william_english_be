"""
Tag model.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel
from .deck import deck_tag_association # Import bảng trung gian

class Tag(BaseModel):
    __tablename__ = "tags"
    name = Column(String(100), unique=True, index=True, nullable=False)
    decks = relationship("Deck", secondary=deck_tag_association, back_populates="tags")
