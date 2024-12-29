// 1.5: One Away

// Runtime: O(min(n, m)) - Space: O(1)
function oneAway(s1, s2) {
  if (Math.abs(s1.length - s2.length) > 1) return false

  const longer = s1.length >= s2.length ? s1 : s2
  const shorter = s1.length < s2.length ? s1 : s2
  let differences = 0

  for (const char in shorter) {
    if (!s2.match(longer[char])) differences += 1
  }

  return differences <= 1
}

console.log(oneAway('pale', 'ple'))  // true
console.log(oneAway('pales', 'pale'))  // true
console.log(oneAway('pale', 'bale'))  // true
console.log(oneAway('pale', 'bake'))  // false
