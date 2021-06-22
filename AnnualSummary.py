from ExpenseRecord import ExpenseRecord
from RentalIncomeRecord import RentalIncomeRecord

class AnnualSummary:
    def __init__(self, expense_rec, rental_rec):
        self.__expense_record = expense_rec
        self.__rental_income_record = rental_rec
        self.__net_profit = 0

    def get_net_profit(self):
        self.net_profit = self.rental_income_record.find_total_rent() - self.expense_record.get_total_expenses()
        return self.net_profit

    def print_annual_report(self):
        print('Annual Summary:\n------------------')
        print('Income:\nRent: {}'.format(self.rental_income_record.find_total_rent()))
        print('Expenses:\n{}'.format(self.expense_record.get_expenses_by_categ()))
        print('Balance: {}'.format(self.get_net_profit()))

        

             
