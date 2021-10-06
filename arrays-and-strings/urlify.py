# 1.3: URLify

# Runtime: O(n) - Space: O(n)
def urlify(string: str) -> str:
    url = []

    for s in string.strip():
        url.append("%20" if s.isspace() else s)

    return "".join(url)


print(urlify("Mr John Smith     "))


# A shorter version of above without it getting too difficult to read
# Can return this in one line, but splitting it out is favorable IMO
def urlify2(string: str) -> str:
    url = ["%20" if s.isspace() else s for s in string.strip()]
    return "".join(url)


print(urlify2("Mr John Smith     "))
