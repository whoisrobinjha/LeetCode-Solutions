#LeetCode Problem 74. Search a 2D Matrix Solution
#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) >> 1
            row, col = divmod(mid, n)
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))