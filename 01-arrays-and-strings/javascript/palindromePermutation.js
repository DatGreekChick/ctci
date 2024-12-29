// 1.4: Palindrome Permutation

// Runtime: O(n) - Space: O(n)
function createCounts(str) {
  const counts = {}

  for (const char of str) {
    if (char === ' ') continue;

    const lowercase = char.toLocaleLowerCase();
    counts[lowercase] = (counts[lowercase] || 0) + 1;
  }

  return counts
}

function calculateDeviations(counts) {
  // an even string can't have any deviations
  // an odd string can have exactly one
  let deviations = 0

  for (const char in counts) {
    if (counts[char] % 2 !== 0) deviations += 1
  }

  return deviations
}

function palindromePermutation(str) {
  const counts = createCounts(str)
  const deviations = calculateDeviations(counts)
  const length = str.length - str.match(/\s/g).length

  if (length % 2 === 0) return deviations === 0
  return deviations === 1
}

console.log(palindromePermutation('Tact Coa'))  // true
