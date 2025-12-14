from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import User
from routes.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/db-test')
def test(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"user_count" : len(users)}

@router.get("/inventory")
def get_inventory(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}"}
