from Menu import Menu


class RentalPropertyManagementSystem:
    def __init__(self):
        self.__user_name = 'user'
        self.__password = 'CeCs343!'
        self.__main_menu = Menu()
        self.log_in_menu()

    def log_in_menu(self):
        print('-------------------------\n' +
              'Rental Management System\n'+
              '-------------------------')
        user_choice = -1
        while(user_choice != 0):
            print('1) Log In\n' +
                '2) Change User Name\n' +
                '3) Change Password\n'+
                '0) Quit\n')
            user_choice = self.get_choice()
            if(user_choice == 1):
                if(self.log_in()):
                    print('Logged in..')
                    self.__main_menu.print_menu()

            elif(user_choice == 2):
                if(self.log_in()):
                    self.__user_name = input('Enter your new user name: ')

            elif(user_choice == 3):
                if(self.log_in()):
                    self.__password = input('Enter your new password: ')

            elif(user_choice == 0):
                print('Good Bye!')

    def get_choice(self):
        choice = -1
        while(choice == -1):
            data = input('Enter your choice: ')
            if(data.isdigit()):
                data = int(data)
                if(data >= 0 and data <= 3):
                    choice = data
            if (choice == -1):
                print('Enter a number between 0 and 3... please try again\n')

        return choice


    def log_in(self):
        username = ' '
        password = ' '
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if(username == self.__user_name and password == self.__password):
            return True
        else:
            print('Invalid user name or password...\n')
            return False