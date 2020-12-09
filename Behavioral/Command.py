from abc import ABC, abstractmethod


# Abstract classes


class AbstractCommand(ABC):
    @abstractmethod
    def do(self):
        pass


# Concrete classes


class ConcreteSave(AbstractCommand):
    def do(self):
        self.__save()

    def __save(self):
        print("Save command")


class ConcreteDelete(AbstractCommand):
    def do(self):
        self.__delete()

    def __delete(self):
        print("Delete command")


class ConcreteChange(AbstractCommand):
    def do(self):
        self.__change()

    def __change(self):
        print("Change command")


class CommandQue:
    def __init__(self):
        self.__commands = []

    def add(self, command: AbstractCommand):
        self.__commands.append(command)

    def get(self) -> AbstractCommand:
        if len(self.__commands) > 0:
            return self.__commands.pop()

    def gen(self):
        while len(self.__commands) > 0:
            command: AbstractCommand = self.__commands.pop()
            yield command


# Using


commands = CommandQue()
commands.add(ConcreteSave())
commands.add(ConcreteChange())
commands.add(ConcreteDelete())
commands.add(ConcreteSave())

for c in commands.gen():
    c.do()

commands.add(ConcreteChange())
commands.add(ConcreteChange())
commands.add(ConcreteChange())

for c in commands.gen():
    c.do()