#LeetCode Problem 1499. Max Value of Equation Solution
#https://leetcode.com/problems/max-value-of-equation/

class Solution:
    def findMaxValueOfEquation(self, points, k):
        length = len(points)
        i = 0
        ans = float('-inf')
        flag = 1

        while i < length:
            if flag < i + 1:
                flag = i + 1

            for j in range(flag, length):
                if points[j][0] > points[i][0] + k:
                    break
                if points[i][1] + points[j][1] + points[j][0] - points[i][0] > ans:
                    ans = points[i][1] + points[j][1] + points[j][0] - points[i][0]
                    flag = j

            i += 1

        return ans

points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print(Solution().findMaxValueOfEquation(points, k))