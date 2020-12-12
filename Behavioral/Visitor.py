from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Abstract classes


class AbstractPlace(ABC):
    @abstractmethod
    def visit_request(self, visitor: AbstractVisitor):
        pass


class AbstractVisitor(ABC):
    @abstractmethod
    def visit_concrete_place_a(self, place: ConcretePlaceA):
        pass

    @abstractmethod
    def visit_concrete_place_b(self, place: ConcretePlaceB):
        pass


# Concrete classes


class ConcretePlaceA(AbstractPlace):
    def visit_request(self, visitor: AbstractVisitor):
        visitor.visit_concrete_place_a(self)

    def place_moving_a(self):
        print("A-place moving")


class ConcretePlaceB(AbstractPlace):
    def visit_request(self, visitor: AbstractVisitor):
        visitor.visit_concrete_place_b(self)

    def place_moving_b(self):
        print("B-place moving")


class ConcreteVisitorA(AbstractVisitor):
    def visit_concrete_place_a(self, place: ConcretePlaceA):
        print(f"\nVisitor A")
        place.place_moving_a()

    def visit_concrete_place_b(self, place: ConcretePlaceB):
        print(f"\nVisitor A")
        place.place_moving_b()


class ConcreteVisitorB(AbstractVisitor):
    def visit_concrete_place_a(self, place: ConcretePlaceA):
        print(f"\nVisitor B")
        place.place_moving_a()

    def visit_concrete_place_b(self, place: ConcretePlaceB):
        print(f"\nVisitor B")
        place.place_moving_b()


# Using

place_a: AbstractPlace = ConcretePlaceA()
place_b: AbstractPlace = ConcretePlaceB()
visitor_a: AbstractVisitor = ConcreteVisitorA()
visitor_b: AbstractVisitor = ConcreteVisitorB()

place_a.visit_request(visitor_a)
# Output:
# Visitor A
# A-place moving

place_a.visit_request(visitor_b)
# Output:
# Visitor B
# A-place moving

place_b.visit_request(visitor_a)
# Output:
# Visitor A
# B-place moving

place_b.visit_request(visitor_b)
# Output:
# Visitor B
# B-place moving