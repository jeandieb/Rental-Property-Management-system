from ExpenseRecord import ExpenseRecord
from RentalIncomeRecord import RentalIncomeRecord

class AnnualSummary:
    def __init__(self, expense_rec, rental_rec):
        self.__expense_record = expense_rec
        self.__rental_income_record = rental_rec
        #self.__net_profit = 0

    def print_annual_report(self):
        self.net_profit = 0
        total_rent = self.__rental_income_record.find_total_rent()
        total_expense = self.__expense_record.get_total_expenses()
        self.net_profit = total_rent - total_expense
        print('Annual Summary:\n------------------')
        print('Income:\nRent: {}'.format(total_rent))
        print('Expenses:\n{}'.format(self.__expense_record.get_expenses_by_categ()))
        print('Balance: {}'.format(self.net_profit))

        

             
