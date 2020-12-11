from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep

# Abstract classes


class AbstractHumanState(ABC):
    def __init__(self):
        self.__human = None

    @property
    def human(self) -> AbstractHuman:
        return self.__human

    @human.setter
    def human(self, human: AbstractHuman) -> None:
        self.__human = human

    @abstractmethod
    def do(self):
        pass


class AbstractHuman:
    def __init__(self):
        self._power = 100

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, power: int):
        self._power = power

    @abstractmethod
    def change_state(self, new_state: AbstractHumanState):
        pass

    @abstractmethod
    def live(self):
        pass


# Concrete classes


class ConcreteHuman(AbstractHuman):
    def __init__(self):
        super().__init__()
        self._state = None
        self.change_state(ConcreteFreezeState())

    def change_state(self, new_state: AbstractHumanState):
        self._state = new_state
        self._state.human = self

    def live(self):
        self._state.do()


class ConcreteFreezeState(AbstractHumanState):
    def do(self):
        print(f"Human freeze (power {self.human.power})")


class ConcreteRunState(AbstractHumanState):
    def do(self):
        if self.human.power < 70:
            print("Human can't run anymore")
            self.human.change_state(new_state=ConcreteGoState())
            self.human.live()
            return
        self.human.power -= 10
        print(f"Human run (power {self.human.power})")


class ConcreteGoState(AbstractHumanState):
    def do(self):
        if self.human.power < 40:
            print("Human can't go anymore")
            self.human.change_state(new_state=ConcreteSitState())
            self.human.live()
            return
        self.human.power -= 5
        print(f"Human go (power {self.human.power})")


class ConcreteSitState(AbstractHumanState):
    def do(self):
        power = self.human.power
        if power < 20:
            print("Human can't sit anymore")
            self.human.change_state(new_state=ConcreteSleepState())
            self.human.live()
            return
        self.human.power -= 1
        print(f"Human sit (power {self.human.power})")


class ConcreteSleepState(AbstractHumanState):
    def do(self):
        if self.human.power > 100:
            print("Human can't sleep anymore")
            self.human.change_state(new_state=ConcreteSitState())
            self.human.live()
            return
        self.human.power += 30
        print(f"Human sleep (power {self.human.power})")


# Using


h = ConcreteHuman()
h.live()  # Output: Human freeze (power 100)
h.live()  # Output: Human freeze (power 100)
h.change_state(ConcreteRunState())

for i in range(30):
    sleep(0.2)
    h.live()
# Output:
# Human freeze (power 100)
# Human freeze (power 100)
# Human run (power 90)
# Human run (power 80)
# Human run (power 70)
# Human run (power 60)
# Human can't run anymore
# Human go (power 55)
# Human go (power 50)
# Human go (power 45)
# Human go (power 40)
# Human go (power 35)
# Human can't go anymore
# Human sit (power 34)
# Human sit (power 33)
# Human sit (power 32)
# Human sit (power 31)
# Human sit (power 30)
# Human sit (power 29)
# Human sit (power 28)
# Human sit (power 27)
# Human sit (power 26)
# Human sit (power 25)
# Human sit (power 24)
# Human sit (power 23)
# Human sit (power 22)
# Human sit (power 21)
# Human sit (power 20)
# Human sit (power 19)
# Human can't sit anymore
# Human sleep (power 49)
# Human sleep (power 79)
# Human sleep (power 109)
# Human can't sleep anymore
# Human sit (power 108)
# Human sit (power 107)