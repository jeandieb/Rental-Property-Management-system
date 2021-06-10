#TODO define update apartment

from Apartment import Apartment

class ApartmentList:
    def __init__(self):
        self. __apartment_list = [] #list that will hold the apartments...

    
    def add_apartment(self):
        self.__apartment_list.append(Apartment())

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

        self.__apartment_list.pop(user_choice-1)

        def update_apartment(self): #dummy
            None

    def print_apartment_list(self):
        index = 0
        for apartment in self.__apartment_list:
            index = index + 1
            print('{}) {}'.format(index, apartment.print_appartment()))

    def get_apartment_list(self):
        return self.__apartment_list

