#LeetCode Problem 1295 - Find Numbers with Even Number of Digits Solution
#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count

nums = [12,345,2,6,7896]
print(Solution().findNumbers(nums))