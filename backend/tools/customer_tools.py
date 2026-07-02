from langchain_core.tools import tool

from services.customer_service import (
    fetch_customer,
    fetch_all_customers,
    search_customer_by_name,
    add_customer,
    update_phone,
    activate_customer,
    deactivate_customer,
    remove_customer,
    customer_summary
)


@tool
def get_customer(customer_id: int):
    """Get customer by ID."""
    return fetch_customer(customer_id)


@tool
def get_all_customers():
    """Returns all customers."""
    return fetch_all_customers()


@tool
def search_customer(name: str):
    """Search customer by name."""
    return search_customer_by_name(name)


@tool
def create_customer(name: str, email: str, phone: str):
    """Create a new customer."""
    return add_customer(name, email, phone)


@tool
def update_customer_phone(customer_id: int, phone: str):
    """Update customer phone."""
    return update_phone(customer_id, phone)


@tool
def activate_customer_account(customer_id: int):
    """Activate customer."""
    return activate_customer(customer_id)


@tool
def deactivate_customer_account(customer_id: int):
    """Deactivate customer."""
    return deactivate_customer(customer_id)


@tool
def delete_customer(customer_id: int):
    """Delete customer."""
    return remove_customer(customer_id)


@tool
def customer_complete_summary(customer_id: int):
    """Returns customer, wallet, accounts and orders."""
    return customer_summary(customer_id)