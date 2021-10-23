# 4.5: Validate BST

from graphs import Node


def is_bst(root: Node, minimum: int, maximum: int) -> bool:
    if not root:
        return True

    if (minimum is not None and root.value <= minimum) or (
        maximum is not None and root.value > maximum
    ):
        return False

    left = is_bst(root.left, minimum, root.value)
    right = is_bst(root.right, root.value, maximum)

    return left and right


def validate_bst(root: Node) -> bool:
    return is_bst(root, None, None)


r = Node(8)
r.left = Node(4)
r.left.left = Node(2)
r.left.right = Node(12)
r.right = Node(10)
r.right.right = Node(20)

r2 = Node(8)
r2.left = Node(4)
r2.left.left = Node(2)
r2.left.right = Node(6)
r2.right = Node(10)
r2.right.right = Node(20)

print(validate_bst(r))  # False
print(validate_bst(r2))  # True
