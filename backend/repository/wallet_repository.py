from database import get_connection


def get_wallet(customer_id: int):
    """
    Returns the wallet of a customer.
    """

    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM wallets
        WHERE customer_id = ?
        """,
        (customer_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def get_wallet_by_id(wallet_id: int):
    """
    Returns wallet using wallet_id.
    """

    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM wallets
        WHERE wallet_id = ?
        """,
        (wallet_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def create_wallet(customer_id: int, balance: float = 0):
    """
    Creates a wallet for a customer.
    """

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO wallets(
            customer_id,
            wallet_balance
        )
        VALUES (?, ?)
        """,
        (
            customer_id,
            balance
        )
    )

    conn.commit()

    wallet_id = cursor.lastrowid

    conn.close()

    return wallet_id


def update_wallet_balance(customer_id: int, balance: float):
    """
    Updates wallet balance.
    """

    conn = get_connection()

    conn.execute(
        """
        UPDATE wallets
        SET wallet_balance = ?,
            last_updated = CURRENT_TIMESTAMP
        WHERE customer_id = ?
        """,
        (
            balance,
            customer_id
        )
    )

    conn.commit()

    conn.close()


def add_money(customer_id: int, amount: float):
    """
    Adds money to wallet.
    """

    wallet = get_wallet(customer_id)

    if wallet is None:
        return False

    new_balance = wallet["wallet_balance"] + amount

    update_wallet_balance(customer_id, new_balance)

    return True


def deduct_money(customer_id: int, amount: float):
    """
    Deduct money from wallet.
    """

    wallet = get_wallet(customer_id)

    if wallet is None:
        return False

    if wallet["wallet_balance"] < amount:
        return False

    new_balance = wallet["wallet_balance"] - amount

    update_wallet_balance(customer_id, new_balance)

    return True


def delete_wallet(customer_id: int):
    """
    Deletes customer's wallet.
    """

    conn = get_connection()

    conn.execute(
        """
        DELETE FROM wallets
        WHERE customer_id = ?
        """,
        (customer_id,)
    )

    conn.commit()

    conn.close()


def wallet_exists(customer_id: int):
    """
    Checks if wallet exists.
    """

    conn = get_connection()

    row = conn.execute(
        """
        SELECT 1
        FROM wallets
        WHERE customer_id = ?
        """,
        (customer_id,)
    ).fetchone()

    conn.close()

    return row is not None


def total_wallet_balance():
    """
    Returns total wallet balance across all customers.
    """

    conn = get_connection()

    total = conn.execute(
        """
        SELECT SUM(wallet_balance) AS total
        FROM wallets
        """
    ).fetchone()["total"]

    conn.close()

    return total if total else 0