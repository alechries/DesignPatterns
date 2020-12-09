from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


# Concrete classes


class IncrementalIterator(Iterator):
    def __init__(self, collection: Collection, reverse=False):
        self.__collection = collection
        self.__reverse = reverse
        self.__position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self.__collection[self.__position]
            self.__position += -1 if self.__reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class Collection(Iterable):
    def __init__(self, collection=None):
        if collection is None:
            collection = []
        self.__collection = collection

    def __iter__(self) -> Iterator:
        return IncrementalIterator(self.__collection)

    def __getitem__(self, item: int):
        return self.__collection[item]

    def add_item(self, item: Any):
        self.__collection.append(item)


# Using


c = Collection()
c.add_item(1)
c.add_item(2)
c.add_item(3)
for i in c:
    print(i, end=' ')  # Output: 1 2 3