# 4.6: Successor

from graphs import Node


class NodeWithParent(Node):
    def __init__(self, value):
        super().__init__(value)
        self.parent = None


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


r = NodeWithParent(8)
r.left = NodeWithParent(4)
r.left.parent = r
r.left.left = NodeWithParent(2)
r.left.left.parent = r.left
r.left.right = NodeWithParent(12)
r.left.right.parent = r.left
r.right = NodeWithParent(10)
r.right.parent = r
r.right.right = NodeWithParent(20)
r.right.right.parent = r.right

print(successor(r).value)  # 10
print(successor(r.right).value)  # 20
print(successor(r.left.left).value)  # 4
