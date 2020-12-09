# Concrete classes

class ConcretePhrase:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self):
        print(f"{self.name.capitalize()}, hello")


class ConcreteDecoratorClass(ConcretePhrase):
    def say_hello(self):
        print('*' * len(self.name))
        super().say_hello()
        print('*' * len(self.name))


# Functions


def decorator_func(encapsulated_func):
    def dec():
        print("###")
        encapsulated_func()
        print("###")
    return dec


# Using decorator class

concrete_phrase: ConcretePhrase = ConcreteDecoratorClass("ALEXANDER")
concrete_phrase.say_hello()  # Output: ****************
#                                      Alexander, hello
#                                      ****************

# Using decorator function

func = concrete_phrase.say_hello
func = decorator_func(func)
func()  # Output: ###
#                 ****************
#                 Alexander, hello
#                 ****************
#                 ###
