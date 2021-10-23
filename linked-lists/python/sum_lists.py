# 2.5: Sum Lists

from linked_list import LinkedList, Node

# Runtime: O(n) - Space: O(1)
def sum_lists(n1: Node, n2: Node, carry: int) -> Node:
    if not n1 and not n2 and not carry:
        return None

    result = Node(0)
    value = carry

    if n1:
        value += n1.data

    if n2:
        value += n2.data

    result.data = value % 10

    if n1 or n2:
        more = sum_lists(
            n1.next if n1 else None,
            n2.next if n2 else None,
            1 if value >= 10 else 0,
        )

        result.next = more

    return result


l1 = LinkedList()
l1.add(6)
l1.add(1)
l1.add(7)

l2 = LinkedList()
l2.add(2)
l2.add(9)
l2.add(5)

summed = sum_lists(l1.head, l2.head, 0)
while summed:
    print(summed.data)
    summed = summed.next
