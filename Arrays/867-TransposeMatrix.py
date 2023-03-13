#LeetCode Problem 867 - Transpose Matrix Solution
#https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix):
        return [*zip(*matrix)]
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().transpose(matrix))