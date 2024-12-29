# 2.6: Palindrome

from linked_list import LinkedList, Node

# Runtime: O(n) - Space: O(1)
def get_values(node: Node) -> tuple:
    size = 0
    counts = {}

    while node:
        size += 1
        counts.update({node.data: counts.get(node.data, 0) + 1})
        node = node.next

    return size, counts


def palindrome(node: Node) -> bool:
    size, counts = get_values(node)
    divergences = 0
    even = size % 2 == 0

    # if even, counts must be divisible by 2
    # if odd, there's one difference allowed
    for c in counts:
        odd = counts[c] % 2 != 0

        if even:
            if odd:
                return False
            continue

        if odd:
            divergences += 1

            if divergences > 1:
                return False

    return True


l1 = LinkedList()
l1.add("r")
l1.add("a")
l1.add("c")
l1.add("e")
l1.add("c")
l1.add("a")
l1.add("r")

l2 = LinkedList()
l2.add("r")
l2.add("a")
l2.add("e")
l2.add("b")

l3 = LinkedList()
l3.add("c")
l3.add("i")
l3.add("v")
l3.add("i")
l3.add("c")

print(palindrome(l1.head))  # True
print(palindrome(l2.head))  # False
print(palindrome(l3.head))  # True

# Runtime: O(n) - Space: O(n/2)
def palindrome2(node: Node) -> bool:
    slow = node
    fast = node
    stack = []

    # once fast/fast.next are null, slow is at middle
    # push elements from first half of ll to stack
    while fast and fast.next:
        stack.append(slow.data)

        slow = slow.next
        fast = fast.next.next

    # uneven size, skip the one pivot element
    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()
        if top != slow.data:
            return False

        slow = slow.next

    return True


print("Chapter 2.6 v2")
print(palindrome2(l1.head))  # True
print(palindrome2(l2.head))  # False
print(palindrome2(l3.head))  # True
