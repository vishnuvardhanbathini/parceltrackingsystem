from database import connect, create_tables

create_tables()

class Courier:

    def add_customer(self, name, phone, address):
        con = connect()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO customers(name,phone,address) VALUES(?,?,?)",
            (name, phone, address)
        )
        con.commit()
        result = cur.lastrowid
        con.close()
        return result

    def register_parcel(self, customer_id, destination):
        con = connect()
        cur = con.cursor()
        cur.execute(
            "SELECT customer_id FROM customers WHERE customer_id=?",
            (customer_id,)
        )
        if not cur.fetchone():
            con.close()
            return False

        cur.execute(
            "INSERT INTO parcels(customer_id,destination) VALUES(?,?)",
            (customer_id, destination)
        )
        con.commit()
        result = cur.lastrowid
        con.close()
        return result

    def track_parcel(self, parcel_id):
        con = connect()
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM parcels WHERE parcel_id=?",
            (parcel_id,)
        )
        result = cur.fetchone()
        con.close()
        return result

    def update_status(self, parcel_id, status):
        con = connect()
        cur = con.cursor()
        cur.execute(
            "UPDATE parcels SET status=? WHERE parcel_id=?",
            (status, parcel_id)
        )
        result = cur.rowcount > 0
        con.commit()
        con.close()
        return result

    def view_customers(self):
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM customers")
        result = cur.fetchall()
        con.close()
        return result
