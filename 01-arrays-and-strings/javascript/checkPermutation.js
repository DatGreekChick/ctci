// 1.2: Check Permutation

// Runtime: O(n) - Space: O(1)
function createCounts(s1, s2) {
  const chars = new Array(256).fill(0)

  for (let i = 0; i < s1.length; ++i) {
    chars[s1.charCodeAt(i)] += 1
  }

  for (let i = 0; i < s2.length; ++i) {
    chars[s2.charCodeAt(i)] -= 1
  }

  return chars
}


// Runtime: O(n) - Space: O(1)
function checkPermutations(s1, s2) {
  if (s1.length !== s2.length) return false

  const counts = createCounts(s1, s2)
  for (let i = 0; i < counts.length; ++i) {
    if (counts[i] !== 0) return false
  }

  return true
}


console.log(checkPermutations('abc', 'cab'))  // true
console.log(checkPermutations('test', 'ttew'))  // false
console.log(checkPermutations('geeksforgeeks', 'forgeeksgeeks'))  // true
