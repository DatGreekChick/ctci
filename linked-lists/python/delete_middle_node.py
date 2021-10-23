# 2.3: Delete Middle Node

from linked_list import LinkedList, Node

# Runtime: O(n) - Space: O(1)
def delete_middle_node(node: Node) -> bool:
    if not node or node.next is None:
        return False

    nxt = node.next
    node.data = nxt.data
    node.next = nxt.next
    return True


a = Node("a")
a.next = Node("b")
c = Node("c")
a.next.next = c
c.next = Node("d")
c.next.next = Node("e")
c.next.next.next = Node("f")

delete_middle_node(c)

ll = LinkedList()
ll.head = a
ll.print()
