"""
Realistic seed.py for L2 Database Project
NOTE: This is a starter version. Extend lists as needed.
"""
import sqlite3, random
from datetime import datetime, timedelta

DB_NAME="l2_database.db"
conn=sqlite3.connect(DB_NAME)
cur=conn.cursor()

def dt():
    return (datetime.now()-timedelta(days=random.randint(0,365))).strftime("%Y-%m-%d %H:%M:%S")

customers=[
("Rahul Sharma","rahul.sharma@gmail.com","9876541001","ACTIVE"),
("Priya Verma","priya.verma@gmail.com","9876541002","ACTIVE"),
("Amit Singh","amit.singh@gmail.com","9876541003","INACTIVE"),
("Neha Kapoor","neha.kapoor@gmail.com","9876541004","ACTIVE"),
("Arjun Mehta","arjun.mehta@gmail.com","9876541005","ACTIVE"),
("Sneha Iyer","sneha.iyer@gmail.com","9876541006","ACTIVE"),
("Rohit Gupta","rohit.gupta@gmail.com","9876541007","BLOCKED"),
("Ananya Das","ananya.das@gmail.com","9876541008","ACTIVE"),
("Karan Malhotra","karan.m@gmail.com","9876541009","ACTIVE"),
("Pooja Nair","pooja.nair@gmail.com","9876541010","INACTIVE"),
]

cities=[
("12 MG Road","Bangalore","Karnataka","560001"),
("18 Park Street","Kolkata","West Bengal","700016"),
("22 Connaught Place","Delhi","Delhi","110001"),
("9 Banjara Hills","Hyderabad","Telangana","500034"),
("44 FC Road","Pune","Maharashtra","411004"),
("77 Anna Salai","Chennai","Tamil Nadu","600002"),
("88 SG Highway","Ahmedabad","Gujarat","380015"),
("11 Marine Drive","Mumbai","Maharashtra","400001"),
("15 Civil Lines","Jaipur","Rajasthan","302006"),
("6 Hazratganj","Lucknow","Uttar Pradesh","226001"),
]

products=[
("iPhone 15 Pro","Phone",79999,50),
("Samsung Galaxy S25","Phone",74999,40),
("MacBook Air M4","Laptop",114999,20),
("Dell XPS 13","Laptop",99999,15),
("Sony WH-1000XM5","Accessories",24999,60),
("Boat Rockerz 450","Accessories",1999,200),
("LG OLED 55","TV",89999,10),
("Logitech MX Master 3S","Accessories",8999,80),
("Apple Watch Series 10","Accessories",45999,30),
("Samsung 65 QLED","TV",119999,8),
]

for c in customers:
    cur.execute("INSERT INTO customers(customer_name,email,phone,status,created_at) VALUES(?,?,?,?,?)",(*c,dt()))

for i,c in enumerate(customers,1):
    a=cities[(i-1)%len(cities)]
    cur.execute("INSERT INTO addresses(customer_id,address_line,city,state,country,zipcode) VALUES(?,?,?,?,?,?)",
    (i,a[0],a[1],a[2],"India",a[3]))
    cur.execute("INSERT INTO accounts(customer_id,account_number,account_type,account_status,balance,created_at) VALUES(?,?,?,?,?,?)",
    (i,f"HDFC{100000000+i}","Savings","ACTIVE",round(random.uniform(5000,150000),2),dt()))
    cur.execute("INSERT INTO wallets(customer_id,wallet_balance,last_updated) VALUES(?,?,?)",
    (i,round(random.uniform(0,5000),2),dt()))

for p in products:
    cur.execute("INSERT INTO products(product_name,category,price,stock) VALUES(?,?,?,?)",p)

order_status=["CREATED","PROCESSING","SHIPPED","DELIVERED","CANCELLED"]
payment_modes=["UPI","Credit Card","Debit Card","Net Banking"]

for oid in range(1,31):
    cid=random.randint(1,len(customers))
    total=0
    cur.execute("INSERT INTO orders(customer_id,order_status,payment_status,total_amount,created_at) VALUES(?,?,?,?,?)",
                (cid,random.choice(order_status),"SUCCESS",0,dt()))
    order_id=cur.lastrowid
    for _ in range(random.randint(1,3)):
        pid=random.randint(1,len(products))
        qty=random.randint(1,2)
        price=products[pid-1][2]
        total+=qty*price
        cur.execute("INSERT INTO order_items(order_id,product_id,quantity,price) VALUES(?,?,?,?)",
                    (order_id,pid,qty,price))
    cur.execute("UPDATE orders SET total_amount=? WHERE order_id=?",(total,order_id))
    cur.execute("INSERT INTO payments(order_id,payment_mode,amount,payment_status,payment_time) VALUES(?,?,?,?,?)",
                (order_id,random.choice(payment_modes),total,"SUCCESS",dt()))
    pay=cur.lastrowid
    cur.execute("INSERT INTO transactions(payment_id,bank_reference,gateway_reference,transaction_status,failure_reason,transaction_time) VALUES(?,?,?,?,?,?)",
                (pay,f"HDFCREF{pay}",f"PG{pay}","SUCCESS","",dt()))
    if random.random()<0.2:
        tr=cur.lastrowid
        cur.execute("INSERT INTO refunds(transaction_id,refund_amount,refund_status,refund_date) VALUES(?,?,?,?)",
                    (tr,total,"COMPLETED",dt()))
    cur.execute("INSERT INTO shipments(order_id,courier_name,tracking_number,shipment_status,shipped_date,delivered_date) VALUES(?,?,?,?,?,?)",
                (order_id,"BlueDart",f"TRK{100000+order_id}","DELIVERED",dt(),dt()))
    cur.execute("INSERT INTO audit_logs(table_name,record_id,operation,old_value,new_value,updated_by,updated_at) VALUES(?,?,?,?,?,?,?)",
                ("orders",order_id,"INSERT","","Order Created","SYSTEM",dt()))

conn.commit()
conn.close()
print("Seed completed.")
