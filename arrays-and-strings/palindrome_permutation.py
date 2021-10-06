# 1.4: Palindrome Permutation

import collections


# Runtime: O(n) - Space: O(n)
def create_counts(string: str) -> dict:
    counts = collections.Counter(string.lower())
    counts.pop(" ", None)
    return counts


def calculate_deviations(counts: dict) -> int:
    # an even string can't have any deviations
    # an odd string can have exactly one
    deviations = 0
    for c in counts:
        if counts[c] % 2 != 0:
            deviations += 1

    return deviations


def palindrome_permutation(string: str) -> bool:
    counts = create_counts(string)
    deviations = calculate_deviations(counts)
    length = len(string) - string.count(" ")

    if length % 2 == 0:
        return deviations == 0

    return deviations == 1


print(palindrome_permutation("Tact Coa"))  # True
