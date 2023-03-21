#LeetCode Problem 566 - Reshape the Matrix Solution
#https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        reshaped_mat = [[0] * c for _ in range(r)]
        row, col = 0, 0
        for i in range(m):
            for j in range(n):
                reshaped_mat[row][col] = mat[i][j]
                col += 1
                if col == c:
                    row += 1
                    col = 0
        return reshaped_mat

mat = [[1,2],[3,4]]
r = 1
c = 4
print(Solution().matrixReshape(mat, r, c))