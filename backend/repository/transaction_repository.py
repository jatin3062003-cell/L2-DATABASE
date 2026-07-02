from database import get_connection


def get_all_transactions():

    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM transactions
        ORDER BY transaction_time DESC
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]


def get_transaction(transaction_id):

    conn = get_connection()

    row = conn.execute("""
        SELECT *
        FROM transactions
        WHERE transaction_id=?
    """, (transaction_id,)).fetchone()

    conn.close()

    return dict(row) if row else None


def failed_transactions():

    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM transactions
        WHERE transaction_status='FAILED'
        ORDER BY transaction_time DESC
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]