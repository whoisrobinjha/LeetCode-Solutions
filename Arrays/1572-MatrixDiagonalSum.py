#LeetCode Problem 1572 - Matrix Diagonal Sum Solution
#https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        primary_sum = sum(mat[i][i] for i in range(n))
        secondary_sum = sum(mat[i][n-i-1] for i in range(n) if i != n-i-1)
        return primary_sum + secondary_sum
    
mat = [ [1,2,3],
        [4,5,6],
        [7,8,9] ]

print(Solution().diagonalSum(mat))