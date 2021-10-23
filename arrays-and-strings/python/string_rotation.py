# 1.9: String Rotation


# Runtime: O(n) - Space: O(1)
def is_substring(s1: str, s2: str) -> bool:
    return s2 in s1


# Runtime: O(n) - Space: O(n)
def string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    # Has to do with the rotation point (xy v. yx)
    # If you double the s1 input string, and s2 is a substring,
    # then you'll find s2 somewhere in s1s1
    s1s1 = f"{s1}{s1}"
    return is_substring(s1s1, s2)


print(string_rotation("waterbottle", "erbottlewat"))
