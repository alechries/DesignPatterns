import random

# Concrete classes


class ConcreteSending:
    def sending(self):
        pass


class ConcreteReceiving:
    def receiving(self):
        pass


class ConcreteTransportation:
    def transportation(self):
        pass


class ConcreteDatabase:
    def registration (self):
        pass

    def initialization(self):
        return random.choice([True, False])


class ConcretePostOffice:
    def __init__(self):
        self.__sending_department = ConcreteSending()
        self.__receiving_department = ConcreteReceiving()
        self.__transportation_department = ConcreteTransportation()
        self.__database_department = ConcreteDatabase()

    def new_letter(self):
        if not self.__database_department.initialization():
            self.new_visitor()
        else:
            print("You have been initialized")
        self.__receiving_department.receiving()
        self.__sending_department.sending()
        self.__transportation_department.transportation()
        print("We accepted the letter")

    def new_visitor(self):
        self.__database_department.registration()
        print("You are registered")


# Using


post_office = ConcretePostOffice()
post_office.new_letter()