
from Tenant import Tenant
from sqlite_methods import get_tenants_from_db, save_tenant, remove_tenant

class TenantList:
    def __init__(self):
        self.__tenant_list = [] #list that will hold the tenants...


    def load_tenants_from_db(self):
        tenant_list = get_tenants_from_db()
        for tenant in tenant_list:
            to_be_added = Tenant()
            to_be_added.db_init(tenant[0], tenant[1], tenant[2], tenant[3], tenant[4])
            self.__tenant_list.append(to_be_added)

    def menu(self):
        user_input = -1
        while(user_input != 0):
            user_input = self.get_choice()
            if(user_input == 1):
                self.add_tenant()

            elif(user_input == 2):
                self.remove_tenant()

            elif(user_input == 3):
                self.update_tenant()

            elif(user_input == 4):
                self.print_tenant_list()

            elif(user_input == 0):
                print('loading ...')
                return 


    def get_choice(self):
        user_input = -1
        while(user_input == -1):
            data = input('1) Add Tenant\n'+
                        '2) Remove Tenant\n'+
                        '3) Update Existing Tenant\n'+
                        '4) Print Tenant List\n'+
                        '0) Go Back to Main Menu\n'+
                        'Enter your choice: ')
            if(data.isdigit()):
                data = int(data)
                if (data >= 0 and data <= 4):
                    user_input = data
            if(user_input == -1):
                print('Enter a number between 0 and 4 ... please try again\n')

        return user_input


    def add_tenant(self): ##fix here 
        tenant = Tenant()
        tenant.user_init()
        self.__tenant_list.append(tenant)
        save_tenant(tenant)

    def remove_tenant(self):
        user_choice = -1
        self.print_tenant_list()
        while(user_choice == -1):
            data = input("which tenant would you like to remove? ")
            if(data.isdigit()):
                data = int(data)
                if(data > 0 and data <= len(self.__tenant_list)):
                    user_choice = data
            if (user_choice == -1):
                print('Enter a number between 1 and {}... please try again\n'.format(len(self.__tenant_list)))
        remove_tenant(self.__tenant_list[user_choice-1])
        self.__tenant_list.pop(user_choice-1)

       
    def update_tenant(self):
        user_choice = -1
        self.print_tenant_list()
        while(user_choice == -1):
            data = input("which tenant would you like to edit? ")
            if(data.isdigit()):
                data = int(data)
                if(data > 0 and data <= len(self.__tenant_list)):
                    user_choice = data
            if (user_choice == -1):
                print('Enter a number between 1 and {}... please try again\n'.format(len(self.__tenant_list)))
        
        tenant = self.__tenant_list[user_choice-1]
        remove_tenant(tenant)#remove the tenant and then re add it after getting updated 
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
        save_tenant(tenant)
        print('done')
            

    def get_what_to_update(self):
        choice = -1
        while(choice == -1):
            data = input('1) Update first name\n' + 
                    '2) Update last name\n'+
                    '3) Update phone\n' +
                    '4) Update email\n' +
                    '5) Update SSN\n') # +
                    #'6) Update rent amount\n')
                    
            if(data.isdigit()):
                data = int(data)
                if(data > 0 and data <= 6):
                    choice = data
            if (choice == -1):
                print('Enter a number between 1 and 6... please try again\n')

        return choice

    def print_tenant_list(self):
        if(len(self.__tenant_list) == 0):
            print('Tenant list is empty...\n')
        index = 0
        for tenant in self.__tenant_list:
            index = index + 1
            print('{}) {}'.format(index, tenant.print_tenant()))

    def get_tenant_list(self):
        return self.__tenant_list

