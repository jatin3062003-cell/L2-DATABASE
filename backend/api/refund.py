from fastapi import APIRouter, HTTPException

from services.refund_service import (
    fetch_all_refunds,
    fetch_refund,
    refund_details,
    all_pending_refunds
)

router = APIRouter(
    prefix="/refunds",
    tags=["Refunds"]
)


# --------------------------------------------------
# Get all refunds
# --------------------------------------------------

@router.get("")
def get_refunds():
    return fetch_all_refunds()


# --------------------------------------------------
# Get refund by ID
# --------------------------------------------------

@router.get("/{refund_id}")
def get_refund(refund_id: int):

    refund = fetch_refund(refund_id)

    if refund is None:
        raise HTTPException(
            status_code=404,
            detail="Refund not found"
        )

    return refund


# --------------------------------------------------
# Get refund + transaction details
# --------------------------------------------------

@router.get("/{refund_id}/details")
def get_refund_details(refund_id: int):

    details = refund_details(refund_id)

    if details is None:
        raise HTTPException(
            status_code=404,
            detail="Refund not found"
        )

    return details


# --------------------------------------------------
# Pending refunds
# --------------------------------------------------

@router.get("/pending/list")
def pending():
    return all_pending_refunds()