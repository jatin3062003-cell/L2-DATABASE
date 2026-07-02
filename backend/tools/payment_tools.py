from langchain_core.tools import tool

from services.payment_service import (
    fetch_payment,
    payment_details,
    failed_payment_list
)


@tool
def get_payment(payment_id: int):
    """Get payment."""
    return fetch_payment(payment_id)


@tool
def investigate_payment(order_id: int):
    """Investigate payment."""
    return payment_details(order_id)


@tool
def list_failed_payments():
    """Returns failed payments."""
    return failed_payment_list()