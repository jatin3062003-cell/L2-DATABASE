from repository.transaction_repository import (
    get_all_transactions,
    get_transaction,
    failed_transactions,
)

from repository.payment_repository import get_payment


# --------------------------------------------------
# Get all transactions
# --------------------------------------------------

def fetch_all_transactions():
    return get_all_transactions()


# --------------------------------------------------
# Get single transaction
# --------------------------------------------------

def fetch_transaction(transaction_id):
    return get_transaction(transaction_id)


# --------------------------------------------------
# Transaction + Payment Details
# --------------------------------------------------

def transaction_details(transaction_id):

    transaction = get_transaction(transaction_id)

    if transaction is None:
        return None

    payment = get_payment(transaction["payment_id"])

    return {
        "transaction": transaction,
        "payment": payment
    }


# --------------------------------------------------
# Failed Transactions
# --------------------------------------------------

def failed_transaction_list():
    return failed_transactions()