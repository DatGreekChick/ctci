# Chapter 4.9: BST Sequences

from typing import List

from graphs import Node


def weave_lists(
    first: List[int],
    second: List[int],
    results: List[List[int]],
    prefix: List[int],
) -> None:
    """
    Weave lists together in all possible ways. This algorithm
    works by removing the "head" from one list, recursing, then
    doing the same thing with the other list.
    """
    if not first or not second:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    # Recruse with "head" of first added to the prefix.
    # Removing the "head" will damage first, so we'll need to put
    # it back where we found it afterwards.
    first_head = first.pop(0)
    prefix.append(first_head)
    weave_lists(first, second, results, prefix)
    first.insert(0, first_head)
    prefix.pop()

    # Do the same thing with second, damaging and then restoring the list.
    second_head = second.pop(0)
    prefix.append(second_head)
    weave_lists(first, second, results, prefix)
    second.insert(0, second_head)
    prefix.pop()


def bst_sequences(node: Node) -> List[List[int]]:
    result = []

    if not node:
        result.append([])
        return result

    # Recurse on the left and right subtrees
    left_sequences = bst_sequences(node.left)
    right_sequences = bst_sequences(node.right)

    # Weave together each list from the left and right sides
    for left in left_sequences:
        for right in right_sequences:
            weaved = []
            weave_lists(left, right, weaved, [node.value])
            result.extend(weaved)

    return result


root = Node(2)
root.left = Node(1)
root.right = Node(3)
print(bst_sequences(root))
