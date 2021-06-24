
from datetime import datetime

class Expense:
    def __init__(self):
       #left empty because initialization will be either from user or db and each has its own method... 
        pass


    def db_init(self, amount, payee, payment_date, category):
        self.__amount = amount
        self.__payee = payee
        self.__payment_date = datetime.strptime(payment_date, '%m/%d/%Y')
        self.__category = category

    def user_init(self):
        self.set_amount()
        self.set_payee()
        self.set_payment_date()
        self.set_category()

    def set_amount(self):
        try:
            self.__amount = abs(float(input('Enter the amount paid (positive numebr only): $')))
        except ValueError:
            print('amount can only be numbers (e.g: 12.56)... try again\n')
            self.set_amount()

    def get_amount(self):
        return self.__amount

    def set_payee(self):
        self.__payee = input('Ente the payee name: ')

    def get_payee(self):
        return self.__payee

    def set_payment_date(self):
        user_date = input('Enter payment date(mm/dd/yyyy): ')
        try:
            self.__payment_date = datetime.strptime(user_date, '%m/%d/%Y')
        except ValueError:
            print('Incorrect format... try again\n')
            self.set_payment_date()
    
    def get_payment_date(self):
        return self.__payment_date.date()

    def set_category(self):
        self.__category = input('Enter payment category: ')

    def get_category(self):
        return self.__category

    def print_expense(self):
        return('Amount: ${}\nPayee: {}\nPayment date: {}\nCategory: {}'.format(
            self.__amount, self.__payee, self.get_payment_date(), self.__category))



