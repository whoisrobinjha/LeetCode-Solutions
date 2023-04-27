#LeetCode Problem 66 - Plus One Solution
#https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0] * n

digits = [1,2,3]
print(Solution().plusOne(digits))