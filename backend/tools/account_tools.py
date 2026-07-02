from langchain_core.tools import tool

from services.account_service import (
    fetch_account,
    customer_accounts,
    deposit,
    withdraw
)


@tool
def get_account(account_id: int):
    """Get account."""
    return fetch_account(account_id)


@tool
def get_customer_accounts(customer_id: int):
    """Returns all accounts of a customer."""
    return customer_accounts(customer_id)


@tool
def deposit_money(account_id: int, amount: float):
    """Deposit money."""
    return deposit(account_id, amount)


@tool
def withdraw_money(account_id: int, amount: float):
    """Withdraw money."""
    return withdraw(account_id, amount)