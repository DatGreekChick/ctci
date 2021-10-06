# 1.3: URLify

# Runtime: O(n) - Space: O(n)
def urlify(string: str) -> str:
    url = []

    for s in string.strip():
        url.append("%20" if s.isspace() else s)

    return "".join(url)


print(urlify("Mr John Smith     "))
