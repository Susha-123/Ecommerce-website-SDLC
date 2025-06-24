from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str]

class CategoryOut(CategoryCreate):
    id: UUID

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: int
    image_url: Optional[str]
    category_id: UUID

class ProductOut(ProductCreate):
    id: UUID

    class Config:
        orm_mode = True
