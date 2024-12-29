from enum import Enum


class Node:
    """A binary tree node"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Status(Enum):
    UNVISITED = 1
    VISITING = 2
    VISITED = 3
