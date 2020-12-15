from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Abstract classes


class Component(ABC):
    def __init__(self):
        self._parent = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        pass

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_branch(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"


class Branch(Component):
    def __init__(self) -> None:
        super().__init__()
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_branch(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({','.join(results)})"


# Using


tree = Branch()

branch = Branch()
branch.add(Leaf())
branch.add(Leaf())

tree.add(branch)

branch = Branch()
branch.add(Leaf())
branch.add(Leaf())
branch.add(Leaf())

tree.add(branch)

branch = Branch()
branch.add(Leaf())

tree.add(branch)

print(tree.operation(), end="")  # Output: Branch(Branch(Leaf,Leaf),Branch(Leaf,Leaf,Leaf),Branch(Leaf))