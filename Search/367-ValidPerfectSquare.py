#LeetCode problem 367 - Valid Perfect Square solution
#https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num
        while start <= end:
            mid = (start + end) >> 1
            if mid * mid > num:
                end = mid - 1
            elif mid * mid < num:
                start = mid + 1
            else:
                return True
        return False

print(Solution().isPerfectSquare(16))