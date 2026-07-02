from repository.account_repository import (
    get_account,
    get_accounts_by_customer,
    update_balance
)


def fetch_account(account_id):
    return get_account(account_id)


def customer_accounts(customer_id):
    return get_accounts_by_customer(customer_id)


def deposit(account_id, amount):
    account = get_account(account_id)

    if account is None:
        return "Account not found."

    new_balance = account["balance"] + amount

    update_balance(account_id, new_balance)

    return "Deposit successful."


def withdraw(account_id, amount):
    account = get_account(account_id)

    if account is None:
        return "Account not found."

    if account["balance"] < amount:
        return "Insufficient balance."

    new_balance = account["balance"] - amount

    update_balance(account_id, new_balance)

    return "Withdrawal successful."