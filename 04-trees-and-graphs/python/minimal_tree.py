# 4.2: Minimal Tree

from graphs import Node


def pre_order_traversal(node: Node):
    if node:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def create_minimal_bst(arr: list, start: int, end: int):
    if end < start:
        return None

    mid = int((start + end) / 2)
    n = Node(arr[mid])
    n.left = create_minimal_bst(arr, start, mid - 1)
    n.right = create_minimal_bst(arr, mid + 1, end)
    return n


def minimal_bst(arr: list) -> Node:
    return create_minimal_bst(arr, 0, len(arr) - 1)


h = minimal_bst([1, 2, 3, 4, 5])
pre_order_traversal(h)
