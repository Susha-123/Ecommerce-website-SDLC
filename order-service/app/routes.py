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

@router.post("/orders", response_model=schemas.OrderOut)
def place_order(order_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    order = models.Order(
        user_id=order_data.user_id,
        shipping_address=order_data.shipping_address,
        payment_mode=order_data.payment_mode
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in order_data.items:
        order_item = models.OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(order_item)

    db.commit()
    db.refresh(order)
    return order

@router.get("/orders/{user_id}", response_model=List[schemas.OrderOut])
def get_orders(user_id: str, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()

@router.get("/orders/details/{order_id}", response_model=schemas.OrderOut)
def get_order_detail(order_id: str, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
