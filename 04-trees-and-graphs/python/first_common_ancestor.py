# Chapter 4.8: First Common Ancestor

from graphs import Node


class NodeWithParentRefs(Node):
    def __init__(self, value, parent=None):
        super().__init__(value)
        self.parent = parent


def depth(node: Node) -> int:
    d = 0
    while node:
        node = node.parent
        d += 1

    return d


def move_up(node: Node, delta: int) -> Node:
    while delta and node:
        node = node.parent
        delta -= 1

    return node


def first_common_ancestor(p: Node, q: Node) -> Node:
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p  # shallower
    second = p if delta > 0 else q  # deeper
    second = move_up(second, abs(delta))

    while first != second and first and second:
        first = first.parent
        second = second.parent

    if first:
        return first
    if second:
        return second

    return first


# or, even better, without parent references
def covers(root: Node, p: Node) -> bool:
    if not root:
        return False

    if root == p:
        return True

    return covers(root.left, p) or covers(root.right, p)


def ancestor_helper(root: Node, p: Node, q: Node) -> Node:
    if not root or root == p or root == q:
        return root

    p_on_left = covers(root.left, p)
    q_on_left = covers(root.left, q)

    if p_on_left != q_on_left:
        return root

    child_side = root.left if p_on_left else root.right
    return ancestor_helper(child_side, p, q)


def fca(root: Node, p: Node, q: Node) -> Node:
    if not covers(root, p) or not covers(root, q):
        return None

    return ancestor_helper(root, p, q)


t1 = NodeWithParentRefs(20)
left = NodeWithParentRefs(10, t1)
right = NodeWithParentRefs(30, t1)
left_left = NodeWithParentRefs(5, left)
left_right = NodeWithParentRefs(15, left)
t1.left = left
t1.right = right
t1.left.left = left_left
t1.left.left.left = NodeWithParentRefs(3, left_left)
t1.left.left.right = NodeWithParentRefs(7, left_left)
t1.left.right = left_right
t1.left.right.right = NodeWithParentRefs(17, left_right)


print(first_common_ancestor(left_left, left_right).value)  # 10
print(first_common_ancestor(left, right).value)  # 20
print(first_common_ancestor(t1, left_left).value)  # 20
print(first_common_ancestor(left_left.right, right).value)  # 20
print(first_common_ancestor(left_left.left, left_left.right).value)  # 5

t1 = Node(20)
left = Node(10)
right = Node(30)
left_left = Node(5)
left_right = Node(15)
t1.left = left
t1.right = right
t1.left.left = left_left
t1.left.left.left = Node(3)
t1.left.left.right = Node(7)
t1.left.right = left_right
t1.left.right.right = Node(17)

print("4.8 Without Parent References")
print(fca(t1, left_left, left_right).value)  # 10
print(fca(t1, left, right).value)  # 20
print(fca(t1, t1, left_left).value)  # 20
print(fca(t1, left_left.right, right).value)  # 20
print(fca(t1, left_left.left, left_left.right).value)  # 5
