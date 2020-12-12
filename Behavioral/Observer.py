from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
# Abstract classes


class AbstractObserver(ABC):
    @abstractmethod
    def notification(self):
        pass


class AbstractSubject(ABC):
    @abstractmethod
    def notify(self):
        pass

    def subscribe(self, observer: AbstractObserver) -> AbstractSubject:
        pass

    def unsubscribe(self, observer: AbstractObserver):
        pass


# Concrete classes


class ConcreteObserver(AbstractObserver):
    def __init__(self, msg: str):
        self.msg = msg

    def notification(self):
        print(self.msg)


class ConcreteSubject(AbstractSubject):
    def __init__(self):
        self.__observers: List[AbstractObserver] = []

    @staticmethod
    def __notify_personal(observer: AbstractObserver):
        observer.notification()

    def notify(self):
        for observer in self.__observers:
            self.__notify_personal(observer)

    def subscribe(self, observer: AbstractObserver):
        if observer not in self.__observers:
            self.__observers.append(observer)
        return self

    def unsubscribe(self, observer: AbstractObserver):
        self.__observers.remove(observer)


# Using


subject_a = ConcreteSubject()
subject_b = ConcreteSubject()
observer_a = ConcreteObserver('Observer A')
observer_b = ConcreteObserver('Observer B')
observer_c = ConcreteObserver('Observer C')
observer_d = ConcreteObserver('Observer D')

subject_a.subscribe(observer_a).subscribe(observer_b).subscribe(observer_c)
subject_b.subscribe(observer_a).subscribe(observer_d)

subject_a.notify()
# Output:
# Observer A
# Observer B
# Observer C
subject_b.notify()
# Output:
# Observer D