from database import get_connection


def get_item(item_id: int):
    """
    Returns an order item by item ID.
    """
    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM order_items
        WHERE item_id = ?
        """,
        (item_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def get_items(order_id: int):
    """
    Returns all items belonging to an order.
    """
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM order_items
        WHERE order_id = ?
        """,
        (order_id,)
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_items_with_product_details(order_id: int):
    """
    Returns all order items along with product information.
    """
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT
            oi.item_id,
            oi.order_id,
            oi.quantity,
            oi.price,
            p.product_id,
            p.product_name,
            p.category,
            p.stock
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        WHERE oi.order_id = ?
        """,
        (order_id,)
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def add_order_item(
    order_id: int,
    product_id: int,
    quantity: int,
    price: float
):
    """
    Adds a product to an order.
    """
    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO order_items(
            order_id,
            product_id,
            quantity,
            price
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            order_id,
            product_id,
            quantity,
            price
        )
    )

    conn.commit()

    item_id = cursor.lastrowid

    conn.close()

    return item_id


def update_quantity(item_id: int, quantity: int):
    """
    Updates the quantity of an order item.
    """
    conn = get_connection()

    conn.execute(
        """
        UPDATE order_items
        SET quantity = ?
        WHERE item_id = ?
        """,
        (
            quantity,
            item_id
        )
    )

    conn.commit()

    conn.close()


def delete_item(item_id: int):
    """
    Deletes an order item.
    """
    conn = get_connection()

    conn.execute(
        """
        DELETE FROM order_items
        WHERE item_id = ?
        """,
        (item_id,)
    )

    conn.commit()

    conn.close()


def order_total(order_id: int):
    """
    Calculates total value of an order.
    """
    conn = get_connection()

    row = conn.execute(
        """
        SELECT SUM(quantity * price) AS total
        FROM order_items
        WHERE order_id = ?
        """,
        (order_id,)
    ).fetchone()

    conn.close()

    return row["total"] if row["total"] else 0