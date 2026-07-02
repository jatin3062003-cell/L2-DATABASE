from repository.order_repository import (
    get_all_orders,
    get_order,
    get_orders_by_customer,
    update_order_status
)

from repository.order_item_repository import get_items
from repository.payment_repository import get_payment_by_order
from repository.shipment_repository import get_shipment


# --------------------------------------------------
# Get all orders
# --------------------------------------------------

def fetch_all_orders():
    return get_all_orders()


# --------------------------------------------------
# Get single order
# --------------------------------------------------

def fetch_order(order_id):
    return get_order(order_id)


# --------------------------------------------------
# Get orders of a customer
# --------------------------------------------------

def customer_orders(customer_id):
    return get_orders_by_customer(customer_id)


# --------------------------------------------------
# Get items of an order
# --------------------------------------------------

def fetch_order_items(order_id):
    return get_items(order_id)


# --------------------------------------------------
# Get payment of an order
# --------------------------------------------------

def fetch_order_payment(order_id):
    return get_payment_by_order(order_id)


# --------------------------------------------------
# Get shipment of an order
# --------------------------------------------------

def fetch_order_shipment(order_id):
    return get_shipment(order_id)


# --------------------------------------------------
# AI Investigation
# --------------------------------------------------

def investigate_order(order_id):

    order = get_order(order_id)

    if order is None:
        return None

    return {
        "order": order,
        "items": get_items(order_id),
        "payment": get_payment_by_order(order_id),
        "shipment": get_shipment(order_id)
    }


# --------------------------------------------------
# Update status
# --------------------------------------------------

def mark_delivered(order_id):
    update_order_status(order_id, "DELIVERED")
    return "Order marked delivered."