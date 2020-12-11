from typing import List
from copy import copy, deepcopy

# Concrete classes


class ConcreteEntity:
    def __init__(self, your_list: List):
        self.your_list = your_list

    def __copy__(self):
        return self.__class__(copy(self.your_list))

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}
        return self.__class__(self.your_list)


# Using

def print_entity(ent: ConcreteEntity):
    print(f"{ent} - {','.join(map(str, ent.your_list))}")


print("INIT")
entity_a = ConcreteEntity([0, 1])
entity_b = ConcreteEntity([2, 3])
print_entity(entity_a)  # Output entity_a: 0,1
print_entity(entity_b)  # Output entity_b: 2,3

print("COPY")
entity_a = copy(entity_b)
print_entity(entity_a)  # Output entity_a: 2,3
print_entity(entity_b)  # Output entity_b: 2,3

print("CHANGE")
entity_a.your_list[0] = 4
entity_b.your_list[0] = 5
print_entity(entity_a)  # Output entity_a: 4,3
print_entity(entity_b)  # Output entity_b: 5,3

print("DEEPCOPY")
entity_a = deepcopy(entity_b)
print_entity(entity_a)  # Output entity_a: 5,3
print_entity(entity_b)  # Output entity_b: 5,3

print("CHANGE")
entity_a.your_list[0] = 6
entity_b.your_list[1] = 7
print_entity(entity_a)  # Output entity_a: 6,7
print_entity(entity_b)  # Output entity_b: 6,7