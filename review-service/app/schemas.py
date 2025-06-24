from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ReviewCreate(BaseModel):
    user_id: UUID
    product_id: UUID
    rating: int
    comment: Optional[str] = None

class ReviewOut(ReviewCreate):
    id: UUID

    class Config:
        orm_mode = True
