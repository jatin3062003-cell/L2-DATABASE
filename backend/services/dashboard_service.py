from repository.customer_repository import get_all_customers
from repository.order_repository import get_pending_orders
from repository.payment_repository import failed_payments
from repository.refund_repository import pending_refunds


def dashboard():

    customers = get_all_customers()
    orders = get_pending_orders()
    payments = failed_payments()
    refunds = pending_refunds()

    return {
        "total_customers": len(customers),
        "pending_orders": len(orders),
        "failed_payments": len(payments),
        "pending_refunds": len(refunds)
    }