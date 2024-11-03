
class Customer:
    def __init__(self, id, name, address, phone):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__phone = phone

    def __str__(self):
        return "ID : {}\tName : {}\tPhone : {}".format(self.get_id(),self.get_name(),self.get_phone())

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone
