# 1.1: Is Unique

# Runtime: O(n) - Space: O(n)
def is_unique(string: str) -> bool:
    counts = set()

    for s in string:
        if s in counts:
            return False

        counts.add(s)

    return True


# Runtime: O(n log n + n) - Space: O(1)
def is_unique_without_additional_data_structures(string: str) -> bool:
    string.sort()  # O(n log n)
    prev = ""

    for curr in string:  # O(n)
        if curr == prev:
            return False

        prev = curr

    return True
