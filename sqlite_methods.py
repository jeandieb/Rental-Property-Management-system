import sqlite3
import os
from Expense import Expense

conn = sqlite3.connect('rental_management.db')
#conn = sqlite3.connect(':memory:')

c = conn.cursor()

#Run this only the first time running the program
if(os.stat("rental_management.db").st_size == 0):
#if(True):
    #create expenses table
    c.execute("""CREATE TABLE expenses(
            amount REAL,
            payee TEXT,
            date TEXT,
            category TEXT
    ) """)

    #create tenants table 
    c.execute("""CREATE TABLE tenants(
            first_name TEXT,
            last_name TEXT,
            phone TEXT,
            email TEXT,
            SSN TEXT
    ) """)

    #create apartments table
    c.execute("""CREATE TABLE apartments(
            number TEXT,
            address TEXT,
            size REAL,
            num_beds INTEGER,
            num_baths REAL,
            rent REAL,
            rental_status TEXT
    ) """)
    c.execute("""INSERT INTO expenses VALUES (8000, 'Bank', '2020-01-15', 'Mortgage'),
                                           (3500, 'City', '2021-12-30', 'Utilities'),
                                           (2000, 'Lemonade', '2021-7-19', 'Insurance'),
                                           (500, 'Geico', '1919-01-01', 'Insurance')""")

    conn.commit()



def get_expenses_from_db():
    c.execute("SELECT * FROM expenses")
    return c.fetchall()

def save_expense(expense):
    with conn:
        c.execute("INSERT INTO expenses VALUES (:amount, :payee, :date, :category)",
        {'amount': expense.get_amount(), 'payee': expense.get_payee(), 'date': expense.get_payment_date(), 'category': expense.get_category()})

def remove_expense(expense):
    with conn:
        c.execute("DELETE FROM expenses WHERE amount = :amount AND payee = :payee AND date = :date",
        {'amount': expense.get_amount(), 'payee': expense.get_payee(), 'date':expense.get_payment_date()})

def close_db():
    print('db closed')
    conn.close()
