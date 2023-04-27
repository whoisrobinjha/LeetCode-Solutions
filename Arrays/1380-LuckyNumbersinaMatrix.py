#LeetCode Problem 1380 - Lucky Numbers in a Matrix Solution
#https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix):
        ans = []
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])
        for i in range(len(matrix)):
            minMax = float('inf')
            for j in range(len(matrix[i])):
                minMax = min(matrix[i][j], minMax)
            rows[i] = minMax
        for i in range(len(matrix[0])):
            maxMin = 0
            for j in range(len(matrix)):
                maxMin = max(matrix[j][i], maxMin)
            cols[i] = maxMin
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] == cols[j]:
                    ans.append(rows[i])
        return ans

matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(Solution().luckyNumbers(matrix))