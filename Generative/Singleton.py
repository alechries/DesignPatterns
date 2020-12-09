from __future__ import annotations

# Concrete classes


class ConcreteSingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConcreteSingleton(metaclass=ConcreteSingletonMeta):
    def __init__(self, num):
        self.num = num


# Using

singleton_a = ConcreteSingleton(1)
singleton_b = ConcreteSingleton(2)
print(singleton_a.num)  # Output: 1
print(singleton_b.num)  # Output: 1