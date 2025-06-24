from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/reviews", response_model=schemas.ReviewOut)
def submit_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Review).filter(
        models.Review.user_id == review.user_id,
        models.Review.product_id == review.product_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="User has already reviewed this product")

    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/reviews/{product_id}", response_model=list[schemas.ReviewOut])
def list_reviews(product_id: str, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.product_id == product_id).all()
