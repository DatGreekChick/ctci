# 2.7: Intersection

from linked_list import LinkedList, Node

# Runtime: O(A + B) - Space: O(1)
class Result:
    def __init__(self, tail: Node, size: int):
        self.tail = tail
        self.size = size


def get_size_and_tail(node: Node) -> Node:
    size = 0

    while node:
        size += 1

        if not node.next:
            return Result(node, size)

        node = node.next


def get_kth_node(node: Node, difference: int) -> Node:
    curr = node

    while difference > 0 and curr:
        curr = curr.next
        difference -= 1

    return curr


def intersection(n1: Node, n2: Node) -> Node:
    res1 = get_size_and_tail(n1)
    res2 = get_size_and_tail(n2)

    if res1.tail.data != res2.tail.data:
        return None

    shorter = n1 if res1.size < res2.size else n2
    longer = n1 if res1.size >= res2.size else n2

    longer = get_kth_node(longer, abs(res1.size - res2.size))

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return longer


head1 = Node(3)
head1.next = Node(1)
head1.next.next = Node(5)
head1.next.next.next = Node(9)
seven = Node(7)
head1.next.next.next.next = seven
seven.next = Node(2)
seven.next.next = Node(1)

head2 = Node(4)
head2.next = Node(6)
head2.next.next = seven

l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(7)
l1.add(9)
l1.add(5)
l1.add(1)
l1.add(3)

l2 = LinkedList()
l2.add(1)
l2.add(2)
l2.add(7)
l2.add(4)
l2.add(6)

print(intersection(head1, head2).data)
print(intersection(l1.head, l2.head))
