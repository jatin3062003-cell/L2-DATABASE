import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("l2_database.db")
cursor = conn.cursor()
def get_connection():
    conn = sqlite3.connect("l2_database.db")
    conn.row_factory = sqlite3.Row
    return conn
# Enable Foreign Keys
cursor.execute("PRAGMA foreign_keys = ON")

# --------------------------------------------------
# Customers
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    status TEXT DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# --------------------------------------------------
# Addresses
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS addresses(
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    address_line TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    zipcode TEXT,
    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
)
""")

# --------------------------------------------------
# Accounts
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    account_number TEXT UNIQUE,
    account_type TEXT,
    account_status TEXT DEFAULT 'ACTIVE',
    balance REAL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
)
""")

# --------------------------------------------------
# Wallet
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS wallets(
    wallet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    wallet_balance REAL DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
)
""")

# --------------------------------------------------
# Products
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL,
    stock INTEGER
)
""")

# --------------------------------------------------
# Orders
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_status TEXT DEFAULT 'CREATED',
    payment_status TEXT DEFAULT 'PENDING',
    total_amount REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
)
""")

# --------------------------------------------------
# Order Items
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items(
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY(order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
)
""")

# --------------------------------------------------
# Payments
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS payments(
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    payment_mode TEXT,
    amount REAL,
    payment_status TEXT,
    payment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(order_id)
        REFERENCES orders(order_id)
)
""")

# --------------------------------------------------
# Transactions
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_id INTEGER NOT NULL,
    bank_reference TEXT,
    gateway_reference TEXT,
    transaction_status TEXT,
    failure_reason TEXT,
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(payment_id)
        REFERENCES payments(payment_id)
)
""")

# --------------------------------------------------
# Refunds
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS refunds(
    refund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id INTEGER NOT NULL,
    refund_amount REAL,
    refund_status TEXT,
    refund_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(transaction_id)
        REFERENCES transactions(transaction_id)
)
""")

# --------------------------------------------------
# Shipments
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS shipments(
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    courier_name TEXT,
    tracking_number TEXT,
    shipment_status TEXT,
    shipped_date TIMESTAMP,
    delivered_date TIMESTAMP,
    FOREIGN KEY(order_id)
        REFERENCES orders(order_id)
)
""")

# --------------------------------------------------
# Audit Logs
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_logs(
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT,
    record_id INTEGER,
    operation TEXT,
    old_value TEXT,
    new_value TEXT,
    updated_by TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Commit all changes
conn.commit()

print("✅ All tables created successfully!")

conn.close()