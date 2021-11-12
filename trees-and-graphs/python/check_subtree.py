# Chapter 4.10: Check Subtree

import re

from graphs import Node


def get_pre_order_string(node: Node, string: list) -> None:
    if not node:
        string.append("X")
        return

    string.append(str(node.value))
    get_pre_order_string(node.left, string)
    get_pre_order_string(node.right, string)


def check_subtree(t1: Node, t2: Node) -> bool:
    s1 = []
    s2 = []
    get_pre_order_string(t1, s1)
    get_pre_order_string(t2, s2)

    s1 = "".join(s1)
    s2 = "".join(s2)

    pattern = re.compile(s2)
    return pattern.search(s1) is not None


t1 = Node(50)
t1.left = Node(20)
t1.left.left = Node(10)
t1.left.left.right = Node(15)
t1.left.left.left = Node(5)
t1.left.right = Node(25)
t1.right = Node(60)
t1.right.right = Node(70)
t1.right.right.left = Node(65)
t1.right.right.right = Node(80)

t2 = Node(70)
t2.left = Node(65)
t2.right = Node(80)

t3 = Node(4)
t3.left = Node(1)
t3.right = Node(7)

print(check_subtree(t1, t2))  # True
print(check_subtree(t1, t3))  # False
