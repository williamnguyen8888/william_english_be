"""
CRUD operations for Deck model.
"""
from sqlalchemy.orm import Session
from app.crud.base_crud import CRUDBase
from app.models.deck import Deck
from app.schemas.deck_schema import DeckCreate, DeckUpdate
from typing import List

class CRUDDeck(CRUDBase[Deck, DeckCreate, DeckUpdate]):
    # Thêm các phương thức đặc thù cho Deck nếu cần, ví dụ:
    def get_decks_by_owner(self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100) -> List[Deck]:
        return db.query(self.model).filter(self.model.owner_id == owner_id).offset(skip).limit(limit).all()
    
    # Có thể thêm các phương thức khác như:
    # - get_deck_with_tags
    # - get_deck_with_notes_and_cards
    # - create_deck_with_tags

deck_crud = CRUDDeck(Deck)
