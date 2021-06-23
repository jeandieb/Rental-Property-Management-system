from ApartmentList import ApartmentList

class RentalIncomeRecord:
    def __init__(self):
        self.__apartment_list = ApartmentList()
        self.__total_rent_received = 0.0


    def menu(self):
        user_input = -1
        while(user_input != 0):     
            user_input = self.get_user_input()
            if(user_input == 1):
                self.__apartment_list.add_apartment()
            
            if(user_input == 2):
                self.__apartment_list.remove_apartment()

            if(user_input == 3):
                self.__apartment_list.update_apartment()

            if(user_input == 4):
                self.__apartment_list.print_apartment_list()

            if(user_input == 5):
                self.generate_income_record()

            if(user_input == 0):
                print('loading...\n')

    def get_user_input(self):
        choice = -1
        while(choice == -1):
            data = input('1) Add Apartment\n' +
                    '2) Remove Apartment\n'+
                    '3) Update Existing Apartment\n'+
                    '4) Print All Available Apartments\n' + 
                    '5) Generate and Print Income Record\n' +
                    '0) Done\n'+
                    'Enter your choice: ')
            if(data.isdigit):
                data = int(data)
                if(data >= 0 and data <= 5):
                    choice = data
            if (choice == -1):
                print('Enter a number between 0 and 5... please try again\n')

        return choice
    
    def generate_income_record(self):
        for apartment in self.__apartment_list.get_apartment_list():
            print(str(apartment.get_number()) + ': ' + str(apartment.get_payments_received()))

    def find_total_rent(self):
        for apartment in self.__apartment_list.get_apartment_list():
            self.__total_rent_received = self.__total_rent_received  + apartment.get_apartment_rent_received_summed()
        return self.__total_rent_received
