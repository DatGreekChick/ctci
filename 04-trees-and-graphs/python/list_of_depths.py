# 4.3: List of Depths

from graphs import Status


class Node:
    def __init__(self, value):
        self.value = value


class LinkedListNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.next = None


class TreeNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.status = Status.UNVISITED
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.depth = 0
        self.size = 0

    def push(self, item):
        node = LinkedListNode(item)
        self.size += 1

        if not self.head:
            self.head = node
            return

        self.head.next = self.head
        self.head = node

    def pop(self):
        item = self.head
        self.head = self.head.next
        return item

    def print(self):
        curr = self.head

        while curr:
            print(f"depth: {self.depth} | node: {curr.value.value}")
            curr = curr.next


def create_linked_lists(root: TreeNode, depths: list, depth: int):
    if not root:
        return

    ll = None

    if len(depths) == depth:
        # need to add depth to depths
        ll = LinkedList()
        ll.depth = depth
        depths.append(ll)
    else:
        ll = depths[depth]

    ll.push(root)
    create_linked_lists(root.left, depths, depth + 1)
    create_linked_lists(root.right, depths, depth + 1)


def list_of_depths(root: TreeNode) -> list:
    depths = []
    create_linked_lists(root, depths, 0)
    return depths


r = TreeNode(8)
r.left = TreeNode(4)
r.left.left = TreeNode(2)
r.left.right = TreeNode(12)
r.right = TreeNode(10)
r.right.right = TreeNode(20)

l = list_of_depths(r)
for elem in l:
    print(elem.print())


def alternate_list_of_depths(root: TreeNode) -> list:
    depths = []
    current = LinkedList()

    if root:
        current.push(root)

    while current.size > 0:
        depths.append(current)
        parent = current.head
        current = LinkedList()

        while parent:
            if parent.value.left:
                current.push(parent.value.left)

            if parent.value.right:
                current.push(parent.value.right)

            parent = parent.next

    return depths


print("Chapter 4.3 Alternative")
l = alternate_list_of_depths(r)
for elem in l:
    print(elem.print())
