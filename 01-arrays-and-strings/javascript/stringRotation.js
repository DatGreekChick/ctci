// 1.9: String Rotation

// Runtime: O(n) - Space: O(n)
function stringRotation(s1, s2) {
  if (s1.length !== s2.length) {
    return false
  }

  // Has to do with the rotation point (xy v. yx)
  // If you double the s1 input string, and s2 is a substring,
  // then you'll find s2 somewhere in s1s1
  const s1s1 = `${s1}${s1}`
  return s1s1.includes(s2)
}


console.log(stringRotation("waterbottle", "erbottlewat"))
