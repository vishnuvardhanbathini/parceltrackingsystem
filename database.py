import sqlite3

def connect():
    return sqlite3.connect("courier.db")

def create_tables():
    con = connect()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS parcels(
        parcel_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        destination TEXT NOT NULL,
        status TEXT DEFAULT 'Booked',
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    )
    """)

    con.commit()
    con.close()
