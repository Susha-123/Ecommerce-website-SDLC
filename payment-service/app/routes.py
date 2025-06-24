from fastapi import APIRouter
from .schemas import PaymentRequest, PaymentResponse
import uuid
import random

router = APIRouter()

@router.post("/pay", response_model=PaymentResponse)
def process_payment(payment: PaymentRequest):
    # Simulate delay or logic if needed
    success = random.choice([True, True, True])  # 75% success rate

    if success:
        return {
            "transaction_id": uuid.uuid4(),
            "status": "Success"
        }
    else:
        return {
            "transaction_id": uuid.uuid4(),
            "status": "Failed"
        }
