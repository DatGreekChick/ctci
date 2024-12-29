// 1.1: Is Unique

// No way to sort strings in JavaScript without turning them into
// arrays first, so O(n) space is the best we can do

// Runtime: O(n log n) - Space: O(n)
function isUnique(str) {
  if (typeof str !== 'string') return false

  // O(n log n)
  const sorted = [...str].sort()

  // O(n)
  for (let i = 0; i < sorted.length; ++i) {
    if (sorted[i] === sorted[i + 1]) return false
  }

  return true
}

console.log(isUnique('eee')) // false
console.log(isUnique('bear')) // true
console.log(isUnique('abca')) // false


// Runtime: O(n) - Space: O(n)
// Could argue that runtime is O(1) if the string only contains ASCII characters
// because you'll never loop through more than 128 chars. If that were the case
// we could return early if the string had a length longer than 128 characters.
function isUniqueOptimized(str) {
  const storage = {}

  for (let i = 0; i < str.length; ++i) {
    if (storage[str[i]]) return false

    storage[str[i]] = 1
  }

  return true
}

console.log(isUniqueOptimized('eee')) // false
console.log(isUniqueOptimized('bear')) // true
console.log(isUniqueOptimized('abca')) // false
