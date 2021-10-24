# 2.4: Partition

from linked_list import LinkedList, Node

# Runtime: O(n) - Space: O(1)
def partition(node: Node, p: int) -> Node:
    head = node
    tail = node

    while node:
        nxt = node.next

        if node.data < p:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node

        node = nxt

    tail.next = None
    return head


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(10)
ll.add(5)
ll.add(8)
ll.add(5)
ll.add(3)

print(partition(ll.head, 5).data)
ll.print()
