import sqlite3
import os
from Expense import Expense
from Tenant import Tenant

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

    #create apartments rent payments table
    c.execute("""CREATE TABLE apartments_rent_payments(
            apartment_num TEXT,
            jan REAL,
            feb REAL,
            mar REAL,
            apr REAL,
            may REAL,
            jun REAL,
            jul REAL,
            aug REAL,
            sep REAL,
            oct REAL,
            nov REAL,
            dec REAL
        ) """)

    c.execute("""INSERT INTO expenses VALUES (8000, 'Bank', '2020-01-15', 'Mortgage'),
                                           (3500, 'City', '2021-12-30', 'Utilities'),
                                           (2000, 'Lemonade', '2021-7-19', 'Insurance'),
                                           (500, 'Geico', '1919-01-01', 'Insurance')""")

    c.execute("""INSERT INTO tenants VALUES ('Jean', 'Dieb', '818-123-4567', 'jeand@abc.com', 'XXX-XX-XXXX'),
                                            ('Manav', 'Dillon', '818-098-7654', 'manavd@abc.com', 'XXX-XX-XXXX'),
                                            ('Al-Muntaser', 'Al-Matani', '818-765-0957', 'almuntasera@abc.com', 'XXX-XX-XXXX'),
                                            ('Phuong', 'Nguyen', '000-000-0000', 'phuongn@abc.com', 'XXX-XX-XXXX')""")

    c.execute("""INSERT INTO apartments VALUES ('141', 'Warren Street, Colton, CA', 1000, 2, 2, 2300, 'False'),
                                              ('551', 'Halifax Drive, Carson, CA', 850, 2, 1, 1900, 'False'),
                                              ('9280', 'Ivy Road Wilmington, CA', 1200, 3, 2.5, 3000, 'False')""")


    c.execute("""INSERT INTO apartments_rent_payments VALUES ('141' ,1000, 1500, 1500, 1000, 800, 1200, 1000, 1500, 1500, 1000, 800, 1200 ),
                                                             ('551', 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900),
                                                             ('9280', 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000)""")
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


def get_tenants_from_db():
    c.execute("SELECT * FROM tenants")
    return c.fetchall()


def save_tenant(tenant):
    with conn:
        c.execute("INSERT INTO tenants VALUES (:first_name, :last_name, :phone, :email, :SSN)",
        {'first_name': tenant.get_first_name(), 'last_name': tenant.get_last_name(), 'phone': tenant.get_phone(),
        'email': tenant.get_email(), 'SSN': tenant.get_SSN()})

def remove_tenant(tenant):
    with conn:
        c.execute("DELETE FROM tenants WHERE last_name = :last_name AND SSN = :SSN",
        {'last_name': tenant.get_last_name(), 'SSN': tenant.get_SSN()})


def get_apartments_form_db():
    c.execute("SELECT * FROM apartments")
    return(c.fetchall())

def save_apartment(apartment):
    with conn:
        c.execute("INSERT INTO apartments VALUES (:number, :address, :size, :num_beds, :num_baths, :rent, :rental_status)",
        {'number': apartment.get_number(), 'address': apartment.get_address(), 'size': apartment.get_size(),
        'num_beds': apartment.get_num_beds(), 'num_baths': apartment.get_num_baths(), 'rent':apartment.get_rent(), 'rental_status':apartment.get_rental_status()})

def remove_apartment(apartment):
    with conn:
        c.execute("DELETE FROM apartments WHERE number = :number AND address = :address AND rent = :rent",
        {'number': apartment.get_number(), 'address': apartment.get_address(), 'rent': apartment.get_rent()})

def get_payments_record_from_db(apartment_num):
    c.execute("SELECT * FROM apartments_rent_payments WHERE apartment_num = :apartment_num", {'apartment_num': apartment_num})
    return (c.fetchone())
    



def close_db():
    print('db closed')
    conn.close()
