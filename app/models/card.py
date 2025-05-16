"""
Card model.
"""
from sqlalchemy import Column, Integer, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import BaseModel

class Card(BaseModel):
    __tablename__ = "cards"
    
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)
    front_content = Column(Text, nullable=False)
    back_content = Column(Text, nullable=False)
    
    # SRS (Spaced Repetition System) fields
    due_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    interval = Column(Integer, default=0, nullable=False)  # Interval in days
    ease_factor = Column(Float, default=2.5, nullable=False)  # Multiplicador for interval
    reps = Column(Integer, default=0, nullable=False)  # Number of repetitions
    
    note = relationship("Note", back_populates="cards")
    review_logs = relationship("ReviewLog", back_populates="card", cascade="all, delete-orphan")
