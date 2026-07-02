from database import get_connection
def get_customer(customer_id: int):
    conn = get_connection()

    row = conn.execute(
        "SELECT * FROM customers WHERE customer_id=?",
        (customer_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def get_all_customers():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM customers ORDER BY customer_name"
    ).fetchall()

    conn.close()

    return [dict(r) for r in rows]


def search_customer(name: str):
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM customers
        WHERE customer_name LIKE ?
        """,
        (f"%{name}%",)
    ).fetchall()

    conn.close()

    return [dict(r) for r in rows]


def create_customer(name, email, phone):
    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO customers
        (customer_name,email,phone)
        VALUES(?,?,?)
        """,
        (name, email, phone)
    )

    conn.commit()

    customer_id = cursor.lastrowid

    conn.close()

    return customer_id


def update_customer_phone(customer_id, phone):
    conn = get_connection()

    conn.execute(
        """
        UPDATE customers
        SET phone=?
        WHERE customer_id=?
        """,
        (phone, customer_id)
    )

    conn.commit()

    conn.close()


def update_customer_status(customer_id, status):
    conn = get_connection()

    conn.execute(
        """
        UPDATE customers
        SET status=?
        WHERE customer_id=?
        """,
        (status, customer_id)
    )

    conn.commit()

    conn.close()


def delete_customer(customer_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM customers WHERE customer_id=?",
        (customer_id,)
    )

    conn.commit()

    conn.close()
    

def get_customer_summary(customer_id):
    conn = get_connection()
    cur = conn.cursor()

    orders = cur.execute(
        "SELECT COUNT(*) FROM orders WHERE customer_id=?",
        (customer_id,)
    ).fetchone()[0]

    accounts = cur.execute(
        "SELECT COUNT(*) FROM accounts WHERE customer_id=?",
        (customer_id,)
    ).fetchone()[0]

    addresses = cur.execute(
        "SELECT COUNT(*) FROM addresses WHERE customer_id=?",
        (customer_id,)
    ).fetchone()[0]

    wallet = cur.execute(
        "SELECT wallet_balance FROM wallets WHERE customer_id=?",
        (customer_id,)
    ).fetchone()

    conn.close()

    return {
        "orders": orders,
        "accounts": accounts,
        "addresses": addresses,
        "wallet_balance": wallet[0] if wallet else 0
    }