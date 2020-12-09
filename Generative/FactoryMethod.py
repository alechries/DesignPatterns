from abc import ABC, abstractmethod

# Abstract classes


class AbstractProduct(ABC):
    @abstractmethod
    def get_num(self):
        pass


class AbstractCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass


# Concrete classes


class ConcreteProduct(AbstractProduct):
    def get_num(self):
        return 0


class ConcreteCreator(AbstractCreator):
    def factory_method(self) -> AbstractProduct:
        return ConcreteProduct()


# Using


creator: AbstractCreator = ConcreteCreator()
product: AbstractProduct = creator.factory_method()
print(product.get_num())  # Output: 0