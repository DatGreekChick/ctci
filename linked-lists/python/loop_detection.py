# 2.8: Loop Detection

from linked_list import LinkedList, Node

# Runtime: O(n) - Space: O(1)
def loop_detection(node: Node) -> Node:
    nodes = set()

    while node:
        if node in nodes:
            return node

        nodes.add(node)
        node = node.next


def loop_detection2(node: Node) -> Node:
    slow = node
    fast = node

    # loop through until they meet at some collision point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # error handling to ensure that there's an actual
    # corrupt linked list
    if not fast or not fast.next:
        return None

    # reset slow to head and move them at same pace
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # return corrupt node (either works)
    return fast


circular = Node("C")
head = Node("A")
head.next = Node("B")
head.next.next = circular
circular.next = Node("D")
circular.next.next = Node("E")
circular.next.next.next = circular


print("Chapter 2.8")
print(loop_detection(head).data)
print("Chapter 2.8 using fast/slow refs")
print(loop_detection2(head).data)
