# 2.1: Remove Dups

from linked_list import LinkedList

# Runtime: O(n) - Space: O(n)
def remove_dups(ll: LinkedList):
    seen = set()
    prev = None
    curr = ll.head

    while curr:
        if curr.data not in seen:
            seen.add(curr.data)
        else:
            prev.next = curr.next

        prev = curr
        curr = curr.next


ll = LinkedList()
ll.add(2)
ll.add(5)
ll.add(3)
ll.add(5)

remove_dups(ll)
ll.print()
