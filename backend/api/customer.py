from fastapi import APIRouter
from services.customer_service import fetch_customer_summary,fetch_customer
from repository.customer_repository import get_all_customers
from repository.account_repository import get_accounts_by_customer
from repository.order_repository import get_orders_by_customer
from repository.wallet_repository import get_wallet
from services.address_service import fetch_customer_addresses


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("")
def all_customers():

        return get_all_customers()


@router.get("/{customer_id}")
def customer(customer_id: int):    
    return fetch_customer(customer_id)
@router.get("/{customer_id}/summary")
def customer_summary(customer_id: int):
    return fetch_customer_summary(customer_id)

@router.get("/{customer_id}/accounts")
def customer_accounts(customer_id: int):
    return get_accounts_by_customer(customer_id)

@router.get("/{customer_id}/orders")
def customer_orders(customer_id: int):
    return get_orders_by_customer(customer_id)
@router.get("/{customer_id}/wallet")
def get_customer_wallet(customer_id: int):
    return get_wallet(customer_id)
@router.get("/{customer_id}/addresses")
def get_customer_address(customer_id: int):
    return fetch_customer_addresses(customer_id)
