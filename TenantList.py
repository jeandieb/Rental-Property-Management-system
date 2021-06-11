
from Tenant import Tenant

class TenantList:
    def __init__(self):
        self.__tenant_list = [] #list that will hold the tenants...

    
    def add_apartment(self):
        self.__apartment_list.append(Tenant())

    def remove_tenant(self):
        user_choice = -1
        self.print_tenant_list()
        while(user_choice == -1):
            data = input("which tenant would you like to remove? ")
            if(data.isdigit):
                data = int(data)
                if(data > 0 and data <= len(self.__tenant_list)):
                    user_choice = data
            if (user_choice == -1):
                print('Enter a number between 1 and {}... please try again\n'.format(len(self.__tenant_list)))

        self.__tenant_list.pop(user_choice-1)

       
    def update_tenant(self):
        user_choice = -1
        self.print_tenant_list()
        while(user_choice == -1):
            data = input("which tenant would you like to edit? ")
            if(data.isdigit):
                data = int(data)
                if(data > 0 and data <= len(self.__apartment_list)):
                    user_choice = data
            if (user_choice == -1):
                print('Enter a number between 1 and {}... please try again\n'.format(len(self.__tenant_list)))
        
        tenant = self.__tenant_list[user_choice-1]
        user_choice = self.get_what_to_update()
        if(user_choice == 1): 
            tenant.set_first_name()
        elif(user_choice == 2):
            tenant.set_last_name()
        elif(user_choice == 3):
            tenant.set_phone()
        elif(user_choice == 4):
            tenant.set_email()
        elif(user_choice == 5):
            tenant.set_SSN()
        elif(user_choice == 6):
            None#tenant.set_apartment() needs to take apartment from the user.. 
        print('done')
            

    def get_what_to_update(self):
        choice = -1
        while(choice == -1):
            data = input('1) Update first name\n' + 
                    '2) Update last name\n'+
                    '3) Update phone\n' +
                    '4) Update number of beds\n' +
                    '5) Update number of baths\n' +
                    '6) Update rent amount\n')
                    
            if(data.isdigit):
                data = int(data)
                if(data > 0 and data <= 6):
                    choice = data
            if (choice == -1):
                print('Enter a number between 1 and 6... please try again\n')

        return choice

    def print_tenant_list(self):
        index = 0
        for apartment in self.__apartment_list:
            index = index + 1
            print('{}) {}'.format(index, apartment.print_appartment()))

    def get_tenant_list(self):
        return self.__tenant_list

