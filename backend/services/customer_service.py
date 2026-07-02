from repository.customer_repository import (
    get_customer,
    get_all_customers,
    search_customer,
    create_customer,
    update_customer_phone,
    update_customer_status,
    delete_customer
)

from repository.account_repository import get_accounts_by_customer
from repository.wallet_repository import get_wallet
from repository.order_repository import get_orders_by_customer
from repository.customer_repository import get_customer_summary

def fetch_customer_summary(customer_id):
    return get_customer_summary(customer_id)
def fetch_customer(customer_id):
    return get_customer(customer_id)


def fetch_all_customers():
    return get_all_customers()


def search_customer_by_name(name):
    return search_customer(name)


def add_customer(name, email, phone):
    return create_customer(name, email, phone)


def update_phone(customer_id, phone):
    update_customer_phone(customer_id, phone)
    return "Phone updated successfully."


def activate_customer(customer_id):
    update_customer_status(customer_id, "ACTIVE")
    return "Customer activated."


def deactivate_customer(customer_id):
    update_customer_status(customer_id, "INACTIVE")
    return "Customer deactivated."


def remove_customer(customer_id):
    delete_customer(customer_id)
    return "Customer deleted."


def customer_summary(customer_id):
    return {
        "customer": get_customer(customer_id),
        "accounts": get_accounts_by_customer(customer_id),
        "wallet": get_wallet(customer_id),
        "orders": get_orders_by_customer(customer_id)
    }