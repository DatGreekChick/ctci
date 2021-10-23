# Chapter 4.4: Check Balanced

import sys

from graphs import Node


def get_depth(root: Node):
    if not root:
        return -1

    dl = get_depth(root.left)
    if dl == sys.maxsize:
        return sys.maxsize

    dr = get_depth(root.right)
    if dr == sys.maxsize:
        return sys.maxsize

    difference = abs(dl - dr)
    if difference > 1:
        return sys.maxsize

    return max(dl, dr) + 1


def check_balanced(root: Node) -> bool:
    return get_depth(root) != sys.maxsize


r = Node(8)
r.left = Node(4)
r.left.left = Node(2)
r.left.right = Node(12)
r.right = Node(10)
r.right.right = Node(20)

r2 = Node(10)
r2.left = Node(5)
r2.right = Node(20)
r2.right.left = Node(3)
r2.right.left.left = Node(9)
r2.right.left.right = Node(18)
r2.right.right = Node(7)

print(check_balanced(r))  # True
print(check_balanced(r2))  # False
