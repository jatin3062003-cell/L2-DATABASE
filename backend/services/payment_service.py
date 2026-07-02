from repository.payment_repository import (
    get_all_payments,
    get_payment,
    get_payment_by_order,
    failed_payments
)

from repository.transaction_repository import get_transaction


# --------------------------------------------------
# Get all payments
# --------------------------------------------------

def fetch_all_payments():
    return get_all_payments()


# --------------------------------------------------
# Get single payment
# --------------------------------------------------

def fetch_payment(payment_id):
    return get_payment(payment_id)


# --------------------------------------------------
# Payment + Transaction Details
# --------------------------------------------------

def payment_details(order_id):

    payment = get_payment_by_order(order_id)

    if payment is None:
        return None

    transaction = get_transaction(payment["payment_id"])

    return {
        "payment": payment,
        "transaction": transaction
    }


# --------------------------------------------------
# Failed Payments
# --------------------------------------------------

def failed_payment_list():
    return failed_payments()