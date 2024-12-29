// 1.8: Zero Matrix

// Runtime: O(n * m) - Space: O(n)
function zeroMatrix(matrix) {
  const cols = []

  matrix.forEach((m, i) => m.forEach((n, j) => {
    if (n === 0) {
      // set entire row to zeros
      matrix[i] = Array(m.length).fill(0)

      // save cols for later
      cols.push(j)
    }
  }))

  for (const col of cols) {
    for (const m of matrix) {
      m[col] = 0
    }
  }

  return matrix
}

console.log(zeroMatrix([[1, 2, 3], [3, 2, 0], [3, 2, 1]]))

// [1,2,3],  =>  [1,2,0],
// [3,2,0],  =>  [0,0,0],
// [3,2,1],  =>  [3,2,0],
