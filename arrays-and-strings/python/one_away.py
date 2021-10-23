# 1.5: One Away

# Runtime: O(n) - Space: O(1) * technically O(n) because of longer/shorter
def one_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    longer = s1 if len(s1) >= len(s2) else s2
    shorter = s1 if len(s1) < len(s2) else s2
    differences = 0

    for s in shorter:
        if s not in longer:
            differences += 1

    return differences <= 1


print(one_away("pale", "ple"))  # True
print(one_away("pales", "pale"))  # True
print(one_away("pale", "bale"))  # True
print(one_away("pale", "bake"))  # False
