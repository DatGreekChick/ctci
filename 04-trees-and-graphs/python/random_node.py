"""
Chapter 4.11: Random Node

The below BST class handles inserting, deleting, and accessing of nodes (the
latter both randomly and in pre-order). There are two ways of handling
randomization here:

(1) In order to have a snappy runtime we store all values, which are - by
definition - unique, in a dictionary pointing to their corresponding nodes. The
storage is O(n), but accessing them randomly happens in O(1). Nice!

(2) We add a size property to the Node class and leverage this data throughout.
This is how it's solved in CTCI, which makes sense because if an interviewer was
only focusing on this one method, (1) would be too simple for the purposes of an
interview.

I've added both, though, because if we needed random access to nodes in a BST,
(1) would be the simplest way of doing it. You're not modifying a typical Node
implementation, and the insertion and deletion methods also remain the same.
Alas, an interview - despite focusing on efficiency of time and space - isn't
always going to fit in real world scenarios.

All other method runtimes are typical of a BST:
    - Height-balanced (best case): O(log n)
    - Average: O(h) where h = height
    - Worst: O(n), where n = total nodes in the tree -> basically a linked list
"""


import random

from graphs import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def _insert(self, parent: Node, node: Node) -> Node:
        if parent.value > node.value:
            if not parent.left:
                parent.left = node
                return node

            return self._insert(parent.left, node)

        else:
            if not parent.right:
                parent.right = node
                return node

            return self._insert(parent.right, node)

        return node

    def insert(self, value: int) -> Node:
        if value in self.nodes:
            return self.nodes[value]

        node = Node(value)
        self.nodes[value] = node

        if not self.root:
            self.root = node
            return node

        return self._insert(self.root, node)

    def find(self, value: int) -> Node:
        return self.nodes.get(value)

    def in_order_predecessor(self, curr: Node) -> int:
        curr = curr.left
        while curr.right:
            curr = curr.right

        return curr.value

    def in_order_successor(self, curr: Node) -> int:
        curr = curr.right
        while curr.left:
            curr = curr.left

        return curr.value

    def _delete(self, value: int, curr: Node) -> Node:
        if value > curr.value:
            curr.right = self._delete(value, curr.right)
        elif value < curr.value:
            curr.left = self._delete(value, curr.left)
        else:
            if not curr.left and not curr.right:
                curr = None
            elif curr.left:
                curr.value = self.in_order_predecessor(curr)
                curr.left = self._delete(curr.value, curr.left)
            else:
                curr.value = self.in_order_successor(curr)
                curr.right = self._delete(curr.value, curr.right)

        return curr

    def delete(self, value) -> Node:
        if not self.find(value):
            return None

        del self.nodes[value]
        return self._delete(value, self.root)

    def get_random_node(self) -> Node:
        if not self.root:
            return None

        random_key = random.choice(list(self.nodes.keys()))
        return self.nodes[random_key]

    def traverse(self, curr: Node) -> None:
        """pre-order traversal"""

        if curr:
            print(curr.value)
            self.traverse(curr.left)
            self.traverse(curr.right)


bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(15)
bst.insert(7)
bst.insert(5)
bst.insert(3)
bst.insert(17)

print("Root node:", bst.root.value)  # 20
print("Random node:", bst.get_random_node().value)  # random!
print("Find non-existent node with value 31:", bst.find(31))  # None
print("Delete non-existent node with value 31:", bst.delete(31))  # None
print("Tree traversal:")
print(bst.traverse(bst.root))
bst.delete(20)
print("Tree traversal after deletion:")
print(bst.traverse(bst.root))
print("Root node:", bst.root.value)

# CTCI IMPLEMENTATION


class TreeNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.size = 1

    def get_ith_node(self, i: int):
        left_size = 0 if not self.left else self.left.size

        if i < left_size:
            return self.left.get_ith_node(i)

        if i == left_size:
            return self

        # skipping over left_size + 1 nodes, so subtract them
        try:
            return self.right.get_ith_node(i - (left_size + 1))
        except AttributeError:
            return None

    def insert_in_order(self, value: int) -> None:
        if value <= self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert_in_order(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert_in_order(value)

        self.size += 1

    def find(self, value: int):
        if value == self.value:
            return self

        if value <= self.value:
            return self.left.find(value) if self.left else None

        if value > self.value:
            return self.right.find(value) if self.right else None

        return None


class Tree:
    def __init__(self):
        self.root = None

    def size(self) -> int:
        return 0 if not self.root else self.root.size

    def get_random_node(self) -> TreeNode:
        if not self.root:
            return None

        idx = random.randint(0, self.size())
        return self.root.get_ith_node(idx)

    def insert_in_order(self, value: int) -> None:
        if not self.root:
            self.root = TreeNode(value)
            return

        self.root.insert_in_order(value)


tree = Tree()
tree.insert_in_order(20)
tree.insert_in_order(10)
tree.insert_in_order(30)
tree.insert_in_order(15)
tree.insert_in_order(7)
tree.insert_in_order(5)
tree.insert_in_order(3)
tree.insert_in_order(17)

print("Cracking the Coding Interview Solution:")
try:
    print(tree.get_random_node().value)
except AttributeError:
    print(None)
