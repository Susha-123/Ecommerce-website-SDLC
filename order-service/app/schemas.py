from pydantic import BaseModel
from typing import List
from uuid import UUID

class OrderItemCreate(BaseModel):
    product_id: UUID
    quantity: int
    price: float

class OrderCreate(BaseModel):
    user_id: UUID
    shipping_address: str
    payment_mode: str
    items: List[OrderItemCreate]

class OrderItemOut(OrderItemCreate):
    id: UUID

    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    id: UUID
    user_id: UUID
    shipping_address: str
    payment_mode: str
    status: str
    items: List[OrderItemOut]

    class Config:
        orm_mode = True
