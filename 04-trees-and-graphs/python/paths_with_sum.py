# Chapter 4.12: Paths with Sum

from graphs import Node


def increment_path_count(path_count: dict, key: int, delta: int) -> None:
    new_count = path_count.get(key, 0) + delta
    if new_count == 0:
        # remove when it hits 0 to reduce space usage
        del path_count[key]
        return

    path_count.update({key: new_count})


def count_paths_with_sum(
    node: Node, target_sum: int, running_sum: int, path_count: dict
) -> int:
    if not node:
        return 0

    # count paths with curr_sum ending at the current node
    running_sum += node.value
    curr_sum = running_sum - target_sum
    total_paths = path_count.get(curr_sum, 0)

    # if running_sum == target_sum, then an additional path starts at root
    # so let's add it
    if running_sum == target_sum:
        total_paths += 1

    # increment path_count, recurse, then decrement path_count
    increment_path_count(path_count, running_sum, 1)
    total_paths += count_paths_with_sum(
        node.left, target_sum, running_sum, path_count
    )
    total_paths += count_paths_with_sum(
        node.right, target_sum, running_sum, path_count
    )
    increment_path_count(path_count, running_sum, -1)

    return total_paths


# Runtime: O(n), where n = # nodes - Space: O(log n)
# Note on space: This can grow to O(n) in an unbalanced binary tree
def paths_with_sum(root: Node, target: int) -> int:
    return count_paths_with_sum(root, target, 0, dict())


root = Node(10)
root.left = Node(5)
root.left.left = Node(3)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right = Node(2)
root.left.right.right = Node(1)
root.right = Node(-3)
root.right.right = Node(11)

print(paths_with_sum(root, 8))  # 3
