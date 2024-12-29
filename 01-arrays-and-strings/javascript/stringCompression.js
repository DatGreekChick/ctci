// 1.6: String Compression

// Runtime: O(n) - Space: O(n)
function stringCompression(str) {
  const compressed = []
  let curr = str[0]
  let count = 0

  for (const char of str) {
    if (char !== curr) {
      compressed.push(`${curr}${count}`)
      curr = char
      count = 1
    } else {
      count++
    }

    if (compressed.length > str.length) return str
  }

  compressed.push(`${curr}${count}`)
  return compressed.join("")
}

console.log(stringCompression("aabcccccaaa"))  // a2b1c5a3
