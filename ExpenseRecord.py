from Expense import Expense

class ExpenseRecord:
    def __init__(self):
        self.__expense_list = [] #list that will hold all the expenses
        self.__expense_by_categ = {}
        self.__total_expenses = 0

    
    def add_expense(self):
        self.__expense_list.append(Expense())
        self.get_total_expenses() #update total
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
        #self.__expense_list.pop(user_choice-1)
        self.get_total_expenses() #update total

       # self.calc_expenses_by_categ()#update categories 


    def print_expense_list(self):
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
