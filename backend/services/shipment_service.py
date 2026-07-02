from repository.shipment_repository import get_shipment


def shipment_details(order_id):
    return get_shipment(order_id)