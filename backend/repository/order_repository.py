from database import get_connection


# --------------------------------------------------
# Get all orders
# --------------------------------------------------

def get_all_orders():
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM orders
        ORDER BY created_at DESC
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]


# --------------------------------------------------
# Get single order
# --------------------------------------------------

def get_order(order_id):
    conn = get_connection()

    row = conn.execute("""
        SELECT *
        FROM orders
        WHERE order_id=?
    """, (order_id,)).fetchone()

    conn.close()

    return dict(row) if row else None


# --------------------------------------------------
# Get customer orders
# --------------------------------------------------

def get_orders_by_customer(customer_id):
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM orders
        WHERE customer_id=?
        ORDER BY created_at DESC
    """, (customer_id,)).fetchall()

    conn.close()

    return [dict(r) for r in rows]


# --------------------------------------------------
# Pending orders
# --------------------------------------------------

def get_pending_orders():
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM orders
        WHERE order_status != 'DELIVERED'
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]


# --------------------------------------------------
# Update status
# --------------------------------------------------

def update_order_status(order_id, status):
    conn = get_connection()

    conn.execute("""
        UPDATE orders
        SET order_status=?
        WHERE order_id=?
    """, (status, order_id))

    conn.commit()
    conn.close()


# --------------------------------------------------
# Delete order
# --------------------------------------------------

def delete_order(order_id):
    conn = get_connection()

    conn.execute("""
        DELETE FROM orders
        WHERE order_id=?
    """, (order_id,))

    conn.commit()
    conn.close()