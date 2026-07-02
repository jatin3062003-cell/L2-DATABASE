from database import get_connection


def get_all_refunds():

    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM refunds
        ORDER BY refund_date DESC
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]


def get_refund(refund_id):

    conn = get_connection()

    row = conn.execute("""
        SELECT *
        FROM refunds
        WHERE refund_id=?
    """, (refund_id,)).fetchone()

    conn.close()

    return dict(row) if row else None


def pending_refunds():

    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM refunds
        WHERE refund_status='INITIATED'
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]