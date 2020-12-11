from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Abstract classes

class AbstractEducationMediator(ABC):
    @abstractmethod
    def notify(self, person: Person):
        pass


class AbstractAdministration(ABC):
    def __init__(self, education_mediator: AbstractEducationMediator):
        self._education_mediator = education_mediator

    @abstractmethod
    def request(self, person):
        pass

# Concrete classes


class Person:
    def __init__(self, person_name: str, person_age: int):
        self.name = person_name
        self.age = person_age


class ConcreteEducationMediator(AbstractEducationMediator):
    def notify(self, person: Person):
        age = person.age
        if age <= 6:
            self.__garden_sanding(person)
        elif age <= 18:
            self.__school_sanding(person)
        elif age <= 25:
            self.__university_sanding(person)
        else:
            self.__work_sanding(person)

    def __sanding_phrase(self, person: Person, to_place: str):
        print(f"Sending {person.name} ({person.age} yo) to {to_place}")

    def __garden_sanding(self, person):
        self.__sanding_phrase(person, 'garden')

    def __school_sanding(self, person):
        self.__sanding_phrase(person, 'school')

    def __university_sanding(self, person):
        self.__sanding_phrase(person, 'university')

    def __work_sanding(self, person):
        self.__sanding_phrase(person, 'work')


class ConcreteAdministrationA(AbstractAdministration):
    def request(self, person):
        print('Request to the administration A')
        self._education_mediator.notify(person)


class ConcreteAdministrationB(AbstractAdministration):
    def request(self, person):
        print('Request to the administration B')
        self._education_mediator.notify(person)

# Using


def request_que(administration: AbstractAdministration, persons: List[Person]):
    for person in persons:
        administration.request(person)


mediator = ConcreteEducationMediator()
administration_a = ConcreteAdministrationA(mediator)
administration_b = ConcreteAdministrationB(mediator)

request_que(
    administration=administration_a,
    persons=[Person('Alex', 16), Person('Fiona', 30), Person('Jon', 5)]
)
# Output:
# Request to the administration A
# Sending Alex (16 yo) to school
# Request to the administration A
# Sending Fiona (30 yo) to work
# Request to the administration A
# Sending Jon (5 yo) to garden

request_que(
    administration=administration_b,
    persons=[Person('Alex', 6), Person('Fiona', 13), Person('Jon', 50)]
)
# Output:
# Request to the administration B
# Sending Alex (6 yo) to garden
# Request to the administration B
# Sending Fiona (13 yo) to school
# Request to the administration B
# Sending Jon (50 yo) to work

