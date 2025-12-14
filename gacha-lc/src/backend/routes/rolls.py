from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Card, InventoryItem
from schemas import RollType, CardRead
from routes.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/roll")
def roll(rolltype: RollType, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    n = rolltype.number
    cards = db.query(Card).filter(func.random()).limit(n).all()
    if len(cards) < 3:
        raise HTTPException(400, "not enough cards")
    for card in cards:
        match = db.query(InventoryItem).filter(InventoryItem.user_id == current_user.id, InventoryItem.card_id == card.id).first()
        if match:
            match.count += 1
        else:
            new_user_card = InventoryItem(current_user.id, card.id)
            db.add(new_user_card)
    db.commit()
    db.close()
    return {"message" : "cards added successfully"}


