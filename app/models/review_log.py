"""
Review log model.
"""
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import BaseModel

class ReviewLog(BaseModel):
    __tablename__ = "review_logs"
    
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    rating = Column(Integer, nullable=False)  # User rating (e.g., 1-4 for difficulty)
    reviewed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Optional: store previous card state for analysis
    previous_interval = Column(Integer, nullable=True)
    previous_ease_factor = Column(Integer, nullable=True)
    
    card = relationship("Card", back_populates="review_logs")
    user = relationship("User", back_populates="review_logs")
