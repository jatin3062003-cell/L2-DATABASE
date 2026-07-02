from langchain_core.tools import tool

from services.shipment_service import shipment_details


@tool
def get_shipment(order_id: int):
    """Returns shipment details."""
    return shipment_details(order_id)