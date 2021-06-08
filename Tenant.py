class Tenant:
    def __init__(self):
        self.__first_name = ''
        self.__last_name = ''
        self.__phone = ''
        self.__email = ''
        self.__SSN = ''
        self.__apartment = None

    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_phone(self, phone):
        self.__phone = phone
    
    def get_phone(self):
        return self.__phone

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_SSN(self, SSN):
        self.__SSN = SSN

    def get_SSN(self):
        return self.__SSN

    def set_apartment(self, apartment):
        self.__apartment = apartment

    def get_apartment(self):
        return self.__apartment

    def print_tenant_apartment_pair(self):
        print(str(self.get_first_name()) + ' ' + str(self.get_last_name()) + '    ' + str(self.__apartment.get_number()))
