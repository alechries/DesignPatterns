from abc import ABC, abstractmethod

# Abstract classes


class AbstractProduct(ABC):
    @abstractmethod
    def get_num(self):
        pass


class AbstractFactory(ABC):
    def factory_method_product_a(self) -> AbstractProduct:
        pass

    def factory_method_product_b(self) -> AbstractProduct:
        pass


# Concrete classes


class ConcreteProductA(AbstractProduct):
    def get_num(self):
        return 0


class ConcreteProductB(AbstractProduct):
    def get_num(self):
        return 1


class ConcreteFactory(AbstractFactory):
    def factory_method_product_a(self) -> AbstractProduct:
        return ConcreteProductA()

    def factory_method_product_b(self) -> AbstractProduct:
        return ConcreteProductB()


# Using


factory: AbstractFactory = ConcreteFactory()
product_a: AbstractProduct = factory.factory_method_product_a()
product_b: AbstractProduct = factory.factory_method_product_b()
print(product_a.get_num())  # Output: 0
print(product_b.get_num())  # Output: 1