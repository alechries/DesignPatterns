# Concrete classes


class ConcreteInteger:
    def get_integer(self):
        return 111


class ConcreteString:
    def get_string(self):
        return "333"


class ConcreteStringToIntegerAdapter(ConcreteInteger):
    def __init__(self, adaptee_string: ConcreteString):
        self.__string = adaptee_string

    def get_integer(self):
        return int(self.__string.get_string())


# Using


string = ConcreteString()
integer = ConcreteStringToIntegerAdapter(string)
print(integer.get_integer())  # Output: 333