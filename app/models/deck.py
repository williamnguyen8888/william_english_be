"""
Deck model.
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import BaseModel

# Bảng trung gian cho quan hệ nhiều-nhiều giữa Deck và Tag
deck_tag_association = Table(
    'deck_tag_association', BaseModel.metadata,
    Column('deck_id', Integer, ForeignKey('decks.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Deck(BaseModel):
    __tablename__ = "decks"
    name = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="decks")
    notes = relationship("Note", back_populates="deck", cascade="all, delete-orphan")
    tags = relationship("Tag", secondary=deck_tag_association, back_populates="decks")
