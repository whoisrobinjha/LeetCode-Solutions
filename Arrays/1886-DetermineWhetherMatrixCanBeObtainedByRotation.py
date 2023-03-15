#LeetCode Problem 1886 - Determine Whether Matrix Can Be Obtained By Rotation Solution
#https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat, target):
        n = len(mat)
        for i in range(4):
            mat = [list(x) for x in zip(*mat[::-1])]
            if mat == target:
                return True
        return False

mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
print(Solution().findRotation(mat, target))