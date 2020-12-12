from typing import List
from time import sleep
import random


# Concrete classes


class Tree:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def get_hash(self):
        return f"_{self.height}_{self.width}"


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class TreeSystem:
    def __init__(self):
        self.trees = {}
        self.coords = {}

    def add_tree(self, coord: Coord, tree: Tree):
        tree_hash = tree.get_hash()
        if tree_hash not in self.trees:
            self.trees[tree_hash] = tree

        if tree_hash not in self.coords:
            self.coords[tree_hash] = [coord, ]
        else:
            trees: List[coord] = self.coords[tree_hash]
            trees.append(coord)

    def del_tree(self, tree: Tree):
        tree_hash = tree.get_hash()

        if tree_hash in self.trees:
            del self.trees[tree_hash]
            del self.coords[tree_hash]

    def print_trees(self):
        for tk, tv in self.trees.items():
            tree_hash: str = tk
            tree: Tree = tv
            tree_coords: List[Coord] = self.coords[tree_hash]
            print(f"\nSelection tree (count {len(tree_coords)})")
            sleep(1)
            print(f"Width {tree.width}")
            sleep(1)
            print(f"Height {tree.height}\n")
            sleep(1)
            for coord in tree_coords:
                print(f"Drawing on coordinates X:{coord.x} Y:{coord.y}")
            sleep(0.4)


# Using


tree_system = TreeSystem()

trees = []
for i in range(3):
    trees.append(Tree(width=random.randint(1, 20), height=random.randint(1, 20)))

for i in range(20):
    coord = Coord(x=i, y=random.randint(1, 100))
    tree_system.add_tree(coord, random.choice(trees))

tree_system.print_trees()


# Output example:
#
# Selection tree (count 7)
# Width 2
# Height 16
#
# Drawing on coordinates X:0 Y:28
# Drawing on coordinates X:1 Y:52
# Drawing on coordinates X:6 Y:22
# Drawing on coordinates X:9 Y:76
# Drawing on coordinates X:12 Y:1
# Drawing on coordinates X:13 Y:36
# Drawing on coordinates X:14 Y:31
#
# Selection tree (count 9)
# Width 14
# Height 5
#
# Drawing on coordinates X:2 Y:47
# Drawing on coordinates X:4 Y:1
# Drawing on coordinates X:5 Y:28
# Drawing on coordinates X:7 Y:18
# Drawing on coordinates X:8 Y:30
# Drawing on coordinates X:10 Y:49
# Drawing on coordinates X:11 Y:21
# Drawing on coordinates X:15 Y:30
# Drawing on coordinates X:19 Y:56
#
# Selection tree (count 4)
# Width 6
# Height 11
#
# Drawing on coordinates X:3 Y:28
# Drawing on coordinates X:16 Y:39
# Drawing on coordinates X:17 Y:45
# Drawing on coordinates X:18 Y:56