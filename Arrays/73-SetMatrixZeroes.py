#LeetCode Problem 73 - Set Matrix Zeroes Solution
#https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(Solution().setZeroes(matrix))