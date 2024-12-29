# 2.2: Return Kth to Last

from linked_list import LinkedList, Node

# Runtime: O(n - k) - Space: O(1)
def return_kth_to_last(kth_idx: int, ll: LinkedList) -> Node:
    size = ll.size
    if size < kth_idx:
        return None

    nodes_left = size - kth_idx
    curr = ll.head

    while curr:
        if nodes_left == 0:
            return curr

        curr = curr.next
        nodes_left -= 1


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)

print(return_kth_to_last(2, ll).data)


# Runtime: O(n - k) - Space: O(1)
def return_kth_to_last_without_size(kth_idx: int, head: Node) -> Node:
    p1 = head
    p2 = head

    for i in range(kth_idx):
        if p1 is None:
            return None
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2


print("Chapter 2.2 without size information")
print(return_kth_to_last_without_size(2, ll.head).data)
