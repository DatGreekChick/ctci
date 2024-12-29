// 1.7: Rotate Matrix

function rotateMatrix(matrix) {
  if (!matrix || matrix.length !== matrix[0].length) {
    return []
  }

  const n = matrix.length
  let layer = 0

  while (layer < n / 2) {
    const first = layer
    const last = n - 1 - layer

    let i = first

    while (i < last) {
      const offset = i - first
      const top = matrix[first][i] // save top

      // left -> top
      matrix[first][i] = matrix[last - offset][first]

      // bottom -> left
      matrix[last - offset][first] = matrix[last][last - offset]

      // right -> bottom
      matrix[last][last - offset] = matrix[i][last]

      // top -> right
      matrix[i][last] = top

      i += 1
    }

    layer += 1
  }

  return matrix
}

console.log(
  rotateMatrix(
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 1, 2, 3],
      [4, 5, 6, 7],
    ]
  )
)

// [1, 2, 3, 4],  =>  [4, 9, 5, 1],
// [5, 6, 7, 8],  =>  [5, 1, 6, 2],
// [9, 1, 2, 3],  =>  [6, 2, 7, 3],
// [4, 5, 6, 7],  =>  [7, 3, 8, 4],
