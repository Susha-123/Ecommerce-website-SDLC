from pydantic import BaseModel
from uuid import UUID

class CartItemCreate(BaseModel):
    user_id: UUID
    product_id: UUID
    quantity: int

class CartItemUpdate(BaseModel):
    quantity: int

class CartItemOut(BaseModel):
    id: UUID
    user_id: UUID
    product_id: UUID
    quantity: int

    class Config:
        orm_mode = True
