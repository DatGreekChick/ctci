# 1.7: Rotate Matrix


def rotate_matrix(matrix: list):
    if not matrix or len(matrix) != len(matrix[0]):
        return []

    n = len(matrix)
    layer = 0

    while layer < n / 2:
        first = layer
        last = n - 1 - layer

        i = first

        while i < last:
            offset = i - first

            # save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

            i += 1

        layer += 1

    return matrix


print(
    rotate_matrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 1, 2, 3],
            [4, 5, 6, 7],
        ]
    )
)

# [1, 2, 3, 4],  =>  [4, 9, 5, 1],
# [5, 6, 7, 8],  =>  [5, 1, 6, 2],
# [9, 1, 2, 3],  =>  [6, 2, 7, 3],
# [4, 5, 6, 7],  =>  [7, 3, 8, 4],
