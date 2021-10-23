# 1.8: Zero Matrix

# Runtime: O(n^2) - Space: O(n)
def zero_matrix(matrix: list):
    cols = []

    for i, m in enumerate(matrix):
        for j, n in enumerate(m):
            if n == 0:
                # set entire row to zeros
                zero_row = [0] * len(m)
                matrix[i] = zero_row

                # save cols for later
                cols.append(j)

    for col in cols:
        for m in matrix:
            m[col] = 0

    return matrix


print(zero_matrix([[1, 2, 3], [3, 2, 0], [3, 2, 1]]))

# [1,2,3],  =>  [1,2,0],
# [3,2,0],  =>  [0,0,0],
# [3,2,1],  =>  [3,2,0],
