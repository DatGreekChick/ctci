# 1.2: Check Permutation

# Runtime: O(n) - Space: O(1)
def create_counts(s1: str, s2: str) -> list:
    chars = [0] * 256

    for s in s1:
        chars[ord(s)] += 1

    for s in s2:
        chars[ord(s)] -= 1

    return chars


# Runtime: O(n) - Space: O(1)
def check_permutations(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    counts = create_counts(s1, s2)
    for c in counts:
        if c != 0:
            return False

    return True


print(check_permutations("abc", "cab"))  # True
print(check_permutations("test", "ttew"))  # False
print(check_permutations("geeksforgeeks", "forgeeksgeeks"))  # True

