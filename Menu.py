from TenantList import TenantList
from RentalIncomeRecord import RentalIncomeRecord
from AnnualSummary import AnnualSummary
from ExpenseRecord import ExpenseRecord

class Menu:
    def __init__(self):
        self.__tenant_list = TenantList()
        self.__rental_rec = RentalIncomeRecord()
        self.__expense_rec = ExpenseRecord()

    def print_menu(self):
        user_choice = -1
        while(user_choice != 0):
            while(user_choice == -1):
                data = input('1) Access Tenant List\n' +
                             '2) Access Rental Income Record\n' +
                             '3) Access Expenses Record\n'+
                             '4) Print Annual Summary\n'+
                             '0) Log Out\n'+
                             'Make a selection: ')
                if (data.isdigit):
                    data = int(data)
                    if(data >= 0 and data <= 4):
                        user_choice = data 

                if(user_choice == -1):
                    print('Invalid input... Enter a number between 0 and 4..\n')

            if(user_choice == 1):
                user_choice = -1
                self.__tenant_list.menu()

            elif(user_choice == 2):
                user_choice = -1
                self.__rental_rec.menu()
            
            elif(user_choice == 3):
                user_choice = -1
                self.__expense_rec.menu()

            elif(user_choice == 4):
                user_choice = -1
                self.__annual_summary = AnnualSummary(self.__expense_rec, self.__rental_rec)
                self.__annual_summary.print_annual_report()

            elif(user_choice == 0):
                print('Logged Out!')
                break