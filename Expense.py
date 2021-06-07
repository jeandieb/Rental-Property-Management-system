import datetime

class Expense:
    def __init__(self):
        self.__amount = 0.0
        self.__payee = ''
        self.__payment_date = datetime.datetime.now() #set to current time by default
        self.__category = ''

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_payee(self, payee):
        self.__payee = payee

    def get_payee(self):
        return self.__payee

    def set_payment_date(self, date):
        self.__payment_date = date
    
    def get_payment_date(self):
        return self.__payment_date

    def set_category(self, category):
        self.__category = category

    def get_category(self):
        return self.__category
