from langchain_core.tools import tool

from services.order_service import (
    fetch_order,
    customer_orders,
    investigate_order,
    mark_delivered
)


@tool
def get_order(order_id: int):
    """Returns order."""
    return fetch_order(order_id)


@tool
def get_customer_orders(customer_id: int):
    """Returns all customer orders."""
    return customer_orders(customer_id)


@tool
def investigate_order_details(order_id: int):
    """
    Complete order investigation.
    Returns payment,
    shipment,
    items.
    """
    return investigate_order(order_id)


@tool
def mark_order_delivered(order_id: int):
    """Mark order delivered."""
    return mark_delivered(order_id)