from fastapi import APIRouter, HTTPException
from uuid import uuid4, UUID
from app.models.payment import Payment, PaymentCreate
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# In-memory store (intentional for learning)
PAYMENTS_DB = {}

@router.post("/payments", response_model=Payment)
def create_payment(payment: PaymentCreate):
    payment_id = uuid4()
    new_payment = Payment(
        id=payment_id,
        amount=payment.amount,
        currency=payment.currency,
        status="CREATED"
    )
    PAYMENTS_DB[payment_id] = new_payment
    logger.info("Payment created Successfully", extra={"payment_id": str(payment_id)})
    return new_payment

@router.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: UUID):
    payment = PAYMENTS_DB.get(payment_id)
    if not payment:
        logger.error("Payment not found", extra={"payment_id": str(payment_id)})
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
