from fastapi import APIRouter

from services.order_service import (
    fetch_all_orders,
    fetch_order,
    fetch_order_items,
    fetch_order_payment,
    fetch_order_shipment,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


# --------------------------------------------------
# Get all orders
# --------------------------------------------------

@router.get("")
def get_orders():
    return fetch_all_orders()


# --------------------------------------------------
# Get order by ID
# --------------------------------------------------

@router.get("/{order_id}")
def get_order(order_id: int):
    return fetch_order(order_id)


# --------------------------------------------------
# Get order items
# --------------------------------------------------

@router.get("/{order_id}/items")
def get_items(order_id: int):
    return fetch_order_items(order_id)


# --------------------------------------------------
# Get payment of an order
# --------------------------------------------------

@router.get("/{order_id}/payment")
def get_payment(order_id: int):
    return fetch_order_payment(order_id)


# --------------------------------------------------
# Get shipment of an order
# --------------------------------------------------

@router.get("/{order_id}/shipment")
def get_shipment(order_id: int):
    return fetch_order_shipment(order_id)