from database import get_connection


def get_shipment(order_id):
    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM shipments
        WHERE order_id=?
        """,
        (order_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None