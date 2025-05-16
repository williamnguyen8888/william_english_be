"""
Note model.
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel

class Note(BaseModel):
    __tablename__ = "notes"
    
    title = Column(String(255), index=True, nullable=False)
    content = Column(Text, nullable=True)  # Hoặc JSON cho cấu trúc phức tạp hơn
    # content = Column(JSON, nullable=True)  # Sử dụng nếu cần lưu cấu trúc JSON
    deck_id = Column(Integer, ForeignKey("decks.id"), nullable=False)
    
    deck = relationship("Deck", back_populates="notes")
    cards = relationship("Card", back_populates="note", cascade="all, delete-orphan")
