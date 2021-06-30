from sqlite_methods import get_payments_record_from_db, save_payments_record

class ApartmentRentPayments:
    def __init__(self, apartment_number):
        self.__apartment_number = apartment_number
        self.__payments_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.__payments_list.insert(0, apartment_number)        
        save_payments_record(self.__payments_list)
        self.__total_rent = 0.0
        my_list = list(get_payments_record_from_db(apartment_number))
        if(my_list): 
            my_list.pop(0)
            self.__payments_list = my_list


    def set_payment_amount(self):
        month = -1
        payment = -1

        while(month == -1):
            data = input('What month the payment is for? (1-12)')
            if(data.isdigit()):
                data = int(data)
                if data > 0 and data < 12:
                    month = data
            if(month == -1):
                print('Please use a number between 1 and 12 for the month... try again\n')
            
        while(payment == -1):
            data1 = input('Enter the amount received: $')
            if(data1.isdigit() and float(data1) > 0):
                payment = float(data1)
            if(payment == -1):
                print('amount can only be numbers and > 0 (e.g: 12.56)... try again\n')


        print('month = ' + str(month))
        print('payment = ' + str(payment))
        self.__payments_list[month-1] = payment


    def get_payments_list(self):
            return self.__payments_list

    def print_payments_list(self):
            print(str(self.__apartment_number) + ': ' + str(self.get_payments_list()))

    def get_apartment_rent_sum(self):
        self.__total_rent = self.calc_total_rent()
        return self.__total_rent
        
    def calc_total_rent(self):
        for num in self.__payments_list:
            self.__total_rent = self.__total_rent + num 
        return self.__total_rent