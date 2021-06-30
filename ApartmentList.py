
from Tenant import Tenant
from Apartment import Apartment
from sqlite_methods import get_apartments_form_db, save_apartment, remove_apartment, get_tenants_from_db


class ApartmentList:
    def __init__(self):
        self.__apartment_list = [] #list that will hold the apartments...


    def load_apartments_from_db(self):
        apartment_list = get_apartments_form_db()
        for apartment in apartment_list:
            to_be_added = Apartment()
            to_be_added.db_init(apartment[0], apartment[1], apartment[2], apartment[3], apartment[4], apartment[5], apartment[6], apartment[7])
            self.__apartment_list.append(to_be_added)
            to_be_added.print_appartment()
    
    def menu(self):
        user_input = -1
        while(user_input != 0):
            while(user_input == -1):
                data = input('1) Add Apartment\n'+
                            '2) Remove Apartment\n'+
                            '3) Update Existing Apartment\n'+
                            '4) Print Apartment List\n'+
                            '0) Go Back to Main Menu\n'+
                            'Enter your choice: ')
                if(data.isdigit):
                    data = int(data)
                    if (data >= 0 and data <= 4):
                        user_input = data
                if(user_input == -1):
                    print('Enter a number between 0 and 4 ... please try again\n')

            if(user_input == 1):
                self.add_apartment()

            elif(user_input == 2):
                self.remove_apartment()

            elif(user_input == 3):
                self.update_apartment()

            elif(user_input == 4):
                self.print_apartment_list()

            elif(user_input == 0):
                print('loading ...')
                break 

    def add_apartment(self):
        apartment = Apartment()
        apartment.user_init()
        self.__apartment_list.append(apartment)
        save_apartment(apartment)

    def remove_apartment(self):
        user_choice = -1
        self.print_apartment_list()
        while(user_choice == -1):
            data = input("which apartment would you like to remove? ")
            if(data.isdigit):
                data = int(data)
                if(data > 0 and data <= len(self.__apartment_list)):
                    user_choice = data
            if (user_choice == -1):
                print('Enter a number between 1 and {}... please try again\n'.format(len(self.__apartment_list)))
        remove_apartment(self.__apartment_list[user_choice-1])
        self.__apartment_list.pop(user_choice-1)

       
    def update_apartment(self):
        user_choice = -1
        self.print_apartment_list()
        while(user_choice == -1):
            data = input("which apartment would you like to edit? ")
            if(data.isdigit):
                data = int(data)
                if(data > 0 and data <= len(self.__apartment_list)):
                    user_choice = data
            if (user_choice == -1):
                print('Enter a number between 1 and {}... please try again\n'.format(len(self.__apartment_list)))
        
        apartment = self.__apartment_list[user_choice-1]
        remove_apartment(apartment)
        user_choice = self.get_what_to_update()
        if(user_choice == 1): 
            apartment.set_number()
        elif(user_choice == 2):
            apartment.set_address()
        elif(user_choice == 3):
            apartment.set_size()
        elif(user_choice == 4):
            apartment.set_num_beds()
        elif(user_choice == 5):
            apartment.set_num_baths()
        elif(user_choice == 6):
            apartment.set_rent()
        elif(user_choice == 7):
            apartment.set__rental_status()
        elif(user_choice == 8):

            tenant_list = get_tenants_from_db()
            tenant_list_objects = []
            for tenant in tenant_list:
                to_be_added = Tenant()
                to_be_added.db_init(tenant[0], tenant[1], tenant[2], tenant[3], tenant[4])
                tenant_list_objects.append(to_be_added)

            i = 0
            for tenant in tenant_list_objects:
                i = i+1
                full_name = tenant.get_first_name() + ' ' + tenant.get_last_name()
                print('{}) {}'.format(i, full_name))
            
            user_choice = -1
            while(user_choice == -1):
                data = input("which tenant would you like to add to this apartment? ")
                if(data.isdigit()):
                    data = int(data)
                    if(data > 0 and data <= len(tenant_list_objects)):
                        user_choice = data
                if (user_choice == -1):
                    print('Enter a number between 1 and {}... please try again\n'.format(len(tenant_list_objects)))
            
            full_name = tenant_list_objects[user_choice -1].get_first_name() + ' ' + tenant_list_objects[user_choice -1].get_last_name()
            apartment.set_tenant(full_name)
       
        elif(user_choice == 9):
            apartment.set_payment_received()
        save_apartment(apartment)
        print('done')
            

    def get_what_to_update(self):
        choice = -1
        while(choice == -1):
            data = input('1) Update number\n' + 
                    '2) Update address\n'+
                    '3) Update size\n' +
                    '4) Update number of beds\n' +
                    '5) Update number of baths\n' +
                    '6) Update rent amount\n' +
                    '7) Update rental status\n' +
                    '8) Update tenant\n' +
                    '9) Update payments record\n'+
                    'Enter your choice: ')
            if(data.isdigit):
                data = int(data)
                if(data > 0 and data <= 9):
                    choice = data
            if (choice == -1):
                print('Enter a number between 1 and 9... please try again\n')

        return choice

    def print_apartment_list(self):
        if(len(self.__apartment_list) == 0):
            print('Apartment list is empty...\n')
        index = 0
        for apartment in self.__apartment_list:
            index = index + 1
            print('{}) {}'.format(index, apartment.print_appartment()))

    def get_apartment_list(self):
        return self.__apartment_list

