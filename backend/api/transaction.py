from fastapi import APIRouter, HTTPException

from services.transaction_service import (
    fetch_all_transactions,
    fetch_transaction,
    transaction_details,
    failed_transaction_list,
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


# --------------------------------------------------
# Get all transactions
# --------------------------------------------------

@router.get("")
def get_transactions():
    return fetch_all_transactions()


# --------------------------------------------------
# Get transaction by ID
# --------------------------------------------------

@router.get("/{transaction_id}")
def get_transaction(transaction_id: int):

    transaction = fetch_transaction(transaction_id)

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


# --------------------------------------------------
# Get transaction details
# --------------------------------------------------

@router.get("/{transaction_id}/details")
def get_transaction_details(transaction_id: int):

    details = transaction_details(transaction_id)

    if details is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return details


# --------------------------------------------------
# Failed Transactions
# --------------------------------------------------

@router.get("/failed/list")
def get_failed_transactions():
    return failed_transaction_list()