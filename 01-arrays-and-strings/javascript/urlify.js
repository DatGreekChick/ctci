// 1.3: URLify

// Runtime: O(n) - Space: O(n)
function urlify(humanStr) {
  const url = []
  const trimmedString = humanStr.trim()

  for (let i = 0; i < trimmedString.length; ++i) {
    url.push(trimmedString[i] === ' ' ? '%20' : trimmedString[i])
  }

  return url.join('')
}

console.log(urlify('mr john smith    '))


// A shorter version of above without it getting too difficult to read
// Can return this in one line, but splitting it out is favorable IMO
const urlify2 = humanStr =>
  humanStr
    .trim()
    .replace(/\s+/g, '%20')


console.log(urlify2('     mr john smith    '))
