from Expense import Expense
from sqlite_methods import get_expenses_from_db, remove_expense, save_expense

class ExpenseRecord:
    def __init__(self):
        self.__expense_list = [] #list that will hold all the expenses
        self.__expense_by_categ = {}
        self.__total_expenses = 0

    
    
    def load_expenses_from_db(self):
        expenses_list = get_expenses_from_db()
        for expense in expenses_list:
            to_be_added = Expense()
            to_be_added.db_init(expense[0], expense[1], expense[2], expense[3])
            self.__expense_list.append(to_be_added)
    
    def menu(self):
        user_input = -1
        while(user_input != 0):
            user_input = self.get_choice()

            if(user_input == 1):
                self.add_expense()

            elif(user_input == 2):
                self.remove_expense()

            elif(user_input == 3):
                self.print_expense_list()

            elif(user_input == 0):
                print('loading ...')
                break     


    def get_choice(self):
        user_input = -1
        while(user_input == -1):
                data = input('1) Add Expense\n'+
                            '2) Remove Expense\n'+
                            '3) Print Expense List\n'+
                            '0) Go Back to Main Menu\n'+
                            'Enter your choice: ')
                if(data.isdigit()):
                    data = int(data)
                    if (data >= 0 and data <= 3):
                        user_input = data
                if(user_input == -1):
                    print('Enter a number between 0 and 3 ... please try again\n')

        return user_input

    def add_expense(self):
        expense = Expense()
        expense.user_init()
        self.__expense_list.append(expense)
        self.get_total_expenses() #update total
        save_expense(expense)
        #self.calc_expenses_by_categ() #update categories 

    def remove_expense(self):
        self.print_expense_list()
        user_choice = -1
        while(user_choice == -1):
            data = input("which expense would you like to remove? ")
            if(data.isdigit):
                data = int(data)
                if(data > 0 and data <= len(self.__expense_list)):
                    user_choice = data
            if (user_choice == -1):
                print('Enter a number between 1 and {}... please try again\n'.format(len(self.__expense_list)))

        self.__total_expenses = self.__total_expenses - self.__expense_list[user_choice-1].get_amount()#udpate total
        remove_expense(self.__expense_list[user_choice-1])
        self.__expense_list.pop(user_choice-1)
        self.get_total_expenses() #update total
        # self.calc_expenses_by_categ()#update categories 


    def print_expense_list(self):
        if(len(self.__expense_list) == 0):
            print('Expense list is empty...\n')
        i = 0
        for expense in self.__expense_list:
            i = i+1
            print('{}) {}'.format(i, expense.print_expense()))

    
    def calc_expenses_by_categ(self):
        self.get_expenses_by_categ = {} #start over, does not update exisiting dict
        for expense in self.__expense_list:
            categ = expense.get_category()
            if(categ in self.__expense_by_categ): 
                self.__expense_by_categ[categ] = self.__expense_by_categ[categ] + expense.get_amount()
            else:
                self.__expense_by_categ.update({categ: expense.get_amount()})



    def get_expense_list(self):
        return self.__expense_list
    
    #ERROR: a second call to get_expenses_by_categ breaks the program "TypeError: 'dict' object is not callable..."
    def get_expenses_by_categ(self):
        self.calc_expenses_by_categ()
        return self.__expense_by_categ

    def get_total_expenses(self):
        self.__total_expenses = 0
        for expense in self.__expense_list:
            self.__total_expenses = self.__total_expenses  + expense.get_amount()
        return self.__total_expenses
