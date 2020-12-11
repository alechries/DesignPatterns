from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep

# Abstract classes


class AbstractHumanState(ABC):
    @abstractmethod
    def do(self):
        pass


class AbstractHuman:
    def __init__(self):
        self.__state = ConcreteFreezeState()

    @property
    def state(self) -> AbstractHumanState:
        return self.__state

    @state.setter
    def state(self, new_state: AbstractHumanState) -> None:
        self.__state = new_state

    @abstractmethod
    def live(self):
        pass


# Concrete classes


class ConcreteHuman(AbstractHuman):
    def live(self):
        self.state.do()


class ConcreteFreezeState(AbstractHumanState):
    def do(self):
        print(f"Human freeze")


class ConcreteRunState(AbstractHumanState):
    def do(self):
        print(f"Human run")


class ConcreteGoState(AbstractHumanState):
    def do(self):
        print(f"Human go")


class ConcreteSitState(AbstractHumanState):
    def do(self):
        print(f"Human sit")


class ConcreteSleepState(AbstractHumanState):
    def do(self):
        print(f"Human sleep")


# Using


h = ConcreteHuman()
h.live()  # Output: Human freeze
h.state = ConcreteRunState()
h.live()  # Output: Human run
h.state = ConcreteGoState()
h.live()  # Output: Human go
h.state = ConcreteSitState()
h.live()  # Output: Human sit
h.state = ConcreteSleepState()
h.live()  # Output: Human sleep
h.state = ConcreteFreezeState()
h.live()  # Output: Human freeze