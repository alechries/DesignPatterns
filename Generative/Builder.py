from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty

# Abstract classes


class AbstractBuilder(ABC):
    @abstractmethod
    def product(self) -> Product:
        pass

    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass


# Concrete classes


class Product:
    def __init__(self):
        self.num_a = None
        self.num_b = None
        self.num_c = None


class ConcreteBuilder(AbstractBuilder):
    def __init__(self):
        self.__product = Product()

    def product(self) -> Product:
        return self.__product

    def build_part_a(self):
        self.__product.num_a = 0

    def build_part_b(self):
        self.__product.num_b = 1

    def build_part_c(self):
        self.__product.num_c = 2


# Using

builder: AbstractBuilder = ConcreteBuilder()
builder.build_part_a()
builder.build_part_b()
product: Product = builder.product()
print(f"Product num - A:{product.num_a}, B:{product.num_b}, C:{product.num_c}")  # Output: Product num - A:0, B:1, C:None