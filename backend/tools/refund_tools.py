from langchain_core.tools import tool

from services.refund_service import (
    refund_details,
    all_pending_refunds
)


@tool
def investigate_refund(transaction_id: int):
    """Investigate refund."""
    return refund_details(transaction_id)


@tool
def list_pending_refunds():
    """Returns pending refunds."""
    return all_pending_refunds()