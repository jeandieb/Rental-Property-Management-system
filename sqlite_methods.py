import sqlite3
import os
from Expense import Expense

conn = sqlite3.connect('rental_management.db')
#conn = sqlite3.connect(':memory:')

c = conn.cursor()

#Run this only when the db is first created 
if(os.stat("rental_management.db").st_size == 0):
#if(True):
    c.execute("""CREATE TABLE expenses(
            amount REAL,
            payee TEXT,
            date TEXT,
            category TEXT
    ) """)

    c.execute("""CREATE TABLE tenants(
            first_name TEXT,
            last_name TEXT,
            phone TEXT,
            email TEXT,
            SSN TEXT
    ) """)

    c.execute("""CREATE TABLE apartments(
            number TEXT,
            address TEXT,
            size REAL,
            num_beds INTEGER,
            num_baths REAL,
            rent REAL,
            rental_status TEXT
    ) """)
    c.execute("""INSERT INTO expenses VALUES (2000, 'Bank', '1/1/2020', 'Mortgage'),
                                           (10000, 'target', '11/12/2020', 'Water')""")

    conn.commit()



def get_expenses_from_db():
    c.execute("SELECT * FROM expenses")
    return c.fetchall()

def close_db():
        print('db closed')
        conn.close()
