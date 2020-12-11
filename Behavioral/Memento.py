from abc import ABC, abstractmethod
from typing import List

# Abstract classes


class AbstractMemento(ABC):
    @abstractmethod
    def get_integer(self) -> int:
        pass


class AbstractStorage(ABC):
    @abstractmethod
    def get(self) -> int:
        pass

    @abstractmethod
    def set(self, value: int):
        pass

    @abstractmethod
    def undo(self) -> AbstractMemento:
        pass

    @abstractmethod
    def backup(self):
        pass

    @abstractmethod
    def history(self) -> List[int]:
        pass


# Concrete classes


class ConcreteMemento(AbstractMemento):
    def __init__(self, state: int):
        self.__state = state

    def get_integer(self) -> int:
        return self.__state


class ConcreteStorage(AbstractStorage):
    def __init__(self, value: int):
        self.__states: List[AbstractMemento] = [ConcreteMemento(value), ]
        self.__current_state: AbstractMemento = ConcreteMemento(value)

    def get(self) -> int:
        return self.__current_state.get_integer()

    def set(self, value: int):
        self.__current_state: AbstractMemento = ConcreteMemento(value)

    def undo(self):
        if len(self.__states) > 0:
            self.__current_state = self.__states.pop(-1)

    def backup(self):
        self.__states.append(self.__current_state)

    def history(self) -> List[int]:
        return [state.get_integer() for state in self.__states]


# Using


storage: AbstractStorage = ConcreteStorage(value=0)
print(storage.history())
# Output: [0]
print(storage.get())
# Output: 0

storage.set(value=1)
# Don't save

storage.set(value=2)
storage.backup()
# Save

storage.set(value=3)
# Don't save

print(storage.history())
# Output: [0, 2]
storage.undo()
print(storage.get())
# Output: 2

print(storage.history())
# Output: [0]
storage.undo()
print(storage.get())
# Output: 0