# 1.3: URLify

# Runtime: O(n) - Space: O(n)
def urlify(string: str) -> str:
    url = []

    for s in string.strip():
        if s == " ":
            url.append("%20")
        else:
            url.append(s)

    return "".join(url)


print(urlify("Mr John Smith     "))

