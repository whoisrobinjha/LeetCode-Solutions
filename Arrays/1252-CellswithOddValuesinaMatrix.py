#LeetCode Problem 1252 - Cells with Odd Values in a Matrix Solution
#https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, m: int, n: int, indices):
        matrix = [[0] * n for _ in range(m)]
        for ri, ci in indices:
            for j in range(n):
                matrix[ri][j] += 1
            for i in range(m):
                matrix[i][ci] += 1
        count = 0
        for row in matrix:
            for cell in row:
                if cell % 2 == 1:
                    count += 1
        
        return count
    
m = 2
n = 3
indices = [[0,1],[1,1]]
print(Solution().oddCells(m, n, indices))