from fastapi import APIRouter, HTTPException

from services.payment_service import (
    fetch_all_payments,
    fetch_payment,
    payment_details,
    failed_payment_list,
)

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


# --------------------------------------------------
# Get all payments
# --------------------------------------------------

@router.get("")
def get_payments():
    return fetch_all_payments()


# --------------------------------------------------
# Get payment by ID
# --------------------------------------------------

@router.get("/{payment_id}")
def get_payment(payment_id: int):

    payment = fetch_payment(payment_id)

    if payment is None:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


# --------------------------------------------------
# Get payment details by Order ID
# --------------------------------------------------

@router.get("/order/{order_id}")
def get_payment_details(order_id: int):

    details = payment_details(order_id)

    if details is None:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return details


# --------------------------------------------------
# Failed payments
# --------------------------------------------------

@router.get("/failed/list")
def get_failed_payments():
    return failed_payment_list()