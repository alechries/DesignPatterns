from abc import ABC, abstractmethod


# Abstract classes


class AbstractEntity(ABC):
    @abstractmethod
    def say_bad_word(self):
        pass


# Concrete classes


class ConcreteEntity(AbstractEntity):
    def __init__(self, bad_word):
        self.__bad_word = bad_word

    def say_bad_word(self):
        print(f"{self.__bad_word} :D")


class ConcreteProxy:
    def __init__(self, real_entity: AbstractEntity):
        self._real_entity = real_entity

    def say_bad_word(self, age: int):
        if self.bad_words_can_be_said(age):
            self._real_entity.say_bad_word()
        else:
            print("You are very young!")

    @staticmethod
    def bad_words_can_be_said(age):
        return age > 16


# Using

entity = ConcreteEntity("BAD WORD")
proxy = ConcreteProxy(entity)
proxy.say_bad_word(20)  # Output: BAD WORD :D
proxy.say_bad_word(12)  # Output: You are very young!
