# 4.6: Successor


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def left_most_child(node: Node) -> Node:
    if not node:
        return None

    while node.left:
        node = node.left

    return node


def successor(node: Node) -> Node:
    if not node:
        return None

    if node.right:
        return left_most_child(node.right)

    q = node
    x = q.parent

    while x and q != x.left:
        q = x
        x = x.parent

    return x


r = Node(8)
r.left = Node(4)
r.left.parent = r
r.left.left = Node(2)
r.left.left.parent = r.left
r.left.right = Node(12)
r.left.right.parent = r.left
r.right = Node(10)
r.right.parent = r
r.right.right = Node(20)
r.right.right.parent = r.right

print(successor(r).value)  # 10
print(successor(r.right).value)  # 20
print(successor(r.left.left).value)  # 4
