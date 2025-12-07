from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/db-test')
def test(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return {"user_count" : len(users)}