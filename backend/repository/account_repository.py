from database import get_connection


def get_account(account_id: int):
    """Get account by account ID."""

    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM accounts
        WHERE account_id = ?
        """,
        (account_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def get_accounts_by_customer(customer_id: int):
    """Get all accounts belonging to a customer."""

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM accounts
        WHERE customer_id = ?
        ORDER BY created_at DESC
        """,
        (customer_id,)
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_account_by_number(account_number: str):
    """Find an account using the account number."""

    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM accounts
        WHERE account_number = ?
        """,
        (account_number,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def create_account(
    customer_id: int,
    account_number: str,
    account_type: str,
    balance: float = 0
):
    """Create a new account."""

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO accounts(
            customer_id,
            account_number,
            account_type,
            balance
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            customer_id,
            account_number,
            account_type,
            balance
        )
    )

    conn.commit()

    account_id = cursor.lastrowid

    conn.close()

    return account_id


def update_balance(account_id: int, balance: float):
    """Update account balance."""

    conn = get_connection()

    conn.execute(
        """
        UPDATE accounts
        SET balance = ?
        WHERE account_id = ?
        """,
        (
            balance,
            account_id
        )
    )

    conn.commit()

    conn.close()


def update_account_status(account_id: int, status: str):
    """Activate/Deactivate account."""

    conn = get_connection()

    conn.execute(
        """
        UPDATE accounts
        SET account_status = ?
        WHERE account_id = ?
        """,
        (
            status,
            account_id
        )
    )

    conn.commit()

    conn.close()


def delete_account(account_id: int):
    """Delete an account."""

    conn = get_connection()

    conn.execute(
        """
        DELETE FROM accounts
        WHERE account_id = ?
        """,
        (account_id,)
    )

    conn.commit()

    conn.close()


def account_exists(account_id: int):
    """Check whether an account exists."""

    conn = get_connection()

    row = conn.execute(
        """
        SELECT 1
        FROM accounts
        WHERE account_id = ?
        """,
        (account_id,)
    ).fetchone()

    conn.close()

    return row is not None


def total_accounts():
    """Return total number of accounts."""

    conn = get_connection()

    count = conn.execute(
        """
        SELECT COUNT(*) as total
        FROM accounts
        """
    ).fetchone()["total"]

    conn.close()

    return count


    conn = get_connection()
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        """
        SELECT *
        FROM accounts
        WHERE customer_id=?
        """,
        (customer_id,)
    ).fetchall()

    conn.close()

    return [dict(r) for r in rows]