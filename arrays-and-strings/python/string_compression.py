# 1.6: String Compression

# Runtime: O(n) - Space: O(n)
def string_compression(string: str) -> str:
    compressed = []
    curr = string[0]
    count = 0

    for s in string:
        if s != curr:
            compressed.append(curr)
            compressed.append(str(count))

            curr = s
            count = 1
        else:
            count += 1

        if len(compressed) > len(string):
            return string

    compressed.append(curr)
    compressed.append(str(count))

    return "".join(compressed)


print(string_compression("aabcccccaaa"))  # a2b1c5a3
