class Apartment:
    def __init__(self):
        self.set_number()
        self.set_address()
        self.set_size()
        self.set_num_beds()
        self.set_num_baths()
        self.set_rent()
        self.set__rental_status()



    def set_number(self):
        self.__number = input('Enter apartment number: ')

    def get_number(self):
        return self.__number

    def set_address(self):
        self.__address = input('Enter apartment address: ')

    def get_address(self):
        return self.__address

    def set_size(self):
        try:
            self.__size = float(input('Enter the apartment size: '))
        except ValueError:
            print('size can only be numbers... try again\n')
            self.set_size()
        
    def get_size(self):
        return self.__size

    def set_num_beds(self):
        try:
            self.__num_beds = int(input('Enter number of bedrooms: '))
        except ValueError:
            print('Number of bedrooms must be an integer... try again\n')
            self.set_num_beds()

    def get_num_beds(self):
        return self.__num_beds

    def set_num_baths(self):
        try:
            self.__num_baths = float(input('Enter number of bathrooms: '))
        except ValueError:
            print('Number of bathrooms must be a number ... try again\n')
            self.set_num_baths()

    def get_num_baths(self):
        return self.__num_baths

    def set_rent(self):
        try:
            self.__rent = float(input('Enter the rent for this apartment: $'))
        except ValueError:
            print('rent can only be numbers (e.g: 12.56)... try again\n')
            self.set_rent()

    def get_rent(self):
        return self.__rent

    def set__rental_status(self):
        user_choice  =  input('Is this apartment rented? (y/n)')
        if(user_choice != 'y' and user_choice != 'n'):
             print('answer with either y or n ... try again\n')
             self.set__rental_status()
       
        else:
            if(user_choice == 'y'): self.__is_rented = True
            elif(user_choice == 'n'): self.__is_rented = False

    def get_rental_status(self):
        return self.__is_rented

    def set_tenant(self, tenant):
        self.__tenant = tenant
        if(tenant == None):
            self.__is_rented = False
        else:
            self.__is_rented = True

    def get_tenant(self):
        return self.__tenant

    def set_payments_received(self, payments):
        self.__payments_received = payments #ApartmentRentPayments()

    def get_payments_received(self):
        return self.__payments_received


    def print_appartment(self):
        return('Apartment number: {} \nAddress: {} \nSize: {} \n# of beds: {}\n# of baths: {} \nRent: {}\nRented? {}'
        .format(self.get_number(), self.get_address(), self.get_size(), self.get_num_beds(), self.get_num_baths(), self.get_rent(), self.get_rental_status()))