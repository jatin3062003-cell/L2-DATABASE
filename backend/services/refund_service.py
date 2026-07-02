from repository.refund_repository import (
    get_all_refunds,
    get_refund,
    pending_refunds
)

from repository.transaction_repository import get_transaction


def fetch_all_refunds():
    return get_all_refunds()


def fetch_refund(refund_id):
    return get_refund(refund_id)


def refund_details(refund_id):

    refund = get_refund(refund_id)

    if refund is None:
        return None

    transaction = get_transaction(refund["transaction_id"])

    return {
        "refund": refund,
        "transaction": transaction
    }


def all_pending_refunds():
    return pending_refunds()