#LeetCode Problem 54 - Spiral Matrix Solution
#https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(Solution().spiralOrder(matrix))