

class Tenant:
    def __init__(self):
        #left empty because initialization will be either from user or db and each has its own method... 
        pass

    def db_init(self, first_name, last_name, phone, email, ssn):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email
        self.__SSN = ssn

    def user_init(self):
        self.set_first_name()
        self.set_last_name()
        self.set_phone()
        self.set_email()
        self.set_SSN()

    def set_first_name(self):
        self.__first_name = input('Enter tenant\'s first name: ')
    
    def get_first_name(self):
        return self.__first_name

    def set_last_name(self):
        self.__last_name =  input('Enter tenant\'s last name: ')

    def get_last_name(self):
        return self.__last_name

    def set_phone(self):
        self.__phone =  input('Enter tenant\'s phone number: ')
    
    def get_phone(self):
        return self.__phone

    def set_email(self):
        self.__email =  input('Enter tenant\'s email address: ')

    def get_email(self):
        return self.__email

    def set_SSN(self):
        self.__SSN =  input('Enter tenant\'s Social Security Number: ')

    def get_SSN(self):
        return self.__SSN

    def set_apartment(self, apartment):
        self.__apartment = apartment
        apartment.set_tenant(self)

    def get_apartment(self):
        return self.__apartment

    def print_tenant_apartment_pair(self):
        print(str(self.get_first_name()) + ' ' + str(self.get_last_name()) + '    ' + str(self.__apartment.get_number()))

    def print_tenant(self):
        return('First name: {} \nLast name: {}\nPhone: {}\nEmail: {}\nSocial Security Number: {}'.format(
            self.__first_name, self.__last_name, self.__phone, self.__email, self.__SSN))