import sqlite3

DB_PATH = "l2_database.db"


from database import get_connection



def get_all_addresses():
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM addresses
        ORDER BY address_id
    """).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_address(address_id: int):
    conn = get_connection()

    row = conn.execute("""
        SELECT *
        FROM addresses
        WHERE address_id=?
    """, (address_id,)).fetchone()

    conn.close()

    if row:
        return dict(row)

    return None


def get_customer_addresses(customer_id: int):
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM addresses
        WHERE customer_id=?
        ORDER BY address_id
    """, (customer_id,)).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def create_address(customer_id, address_line, city, state, country, zipcode):
    conn = get_connection()

    cursor = conn.execute("""
        INSERT INTO addresses(
            customer_id,
            address_line,
            city,
            state,
            country,
            zipcode
        )
        VALUES(?,?,?,?,?,?)
    """, (
        customer_id,
        address_line,
        city,
        state,
        country,
        zipcode
    ))

    conn.commit()

    address_id = cursor.lastrowid

    conn.close()

    return address_id


def update_address(
    address_id,
    address_line,
    city,
    state,
    country,
    zipcode
):
    conn = get_connection()

    conn.execute("""
        UPDATE addresses
        SET
            address_line=?,
            city=?,
            state=?,
            country=?,
            zipcode=?
        WHERE address_id=?
    """, (
        address_line,
        city,
        state,
        country,
        zipcode,
        address_id
    ))

    conn.commit()
    conn.close()

    return True


def delete_address(address_id: int):
    conn = get_connection()

    conn.execute("""
        DELETE FROM addresses
        WHERE address_id=?
    """, (address_id,))

    conn.commit()
    conn.close()

    return True