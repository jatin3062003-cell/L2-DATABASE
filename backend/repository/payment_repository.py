from database import get_connection



def get_all_payments():
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM payments
        ORDER BY payment_time DESC
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]

def get_payment(payment_id):
    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM payments
        WHERE payment_id=?
        """,
        (payment_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def get_payment_by_order(order_id):
    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM payments
        WHERE order_id=?
        """,
        (order_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def failed_payments():
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM payments
        WHERE payment_status='FAILED'
        """
    ).fetchall()

    conn.close()

    return [dict(r) for r in rows]


def pending_payments():
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM payments
        WHERE payment_status='PENDING'
        """
    ).fetchall()

    conn.close()

    return [dict(r) for r in rows]