#LeetCode Problem 1929 - Concatenation of Array Solution
#https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums):
        nums.extend(nums)
        return nums

nums = [1,2,1]
print(Solution().getConcatenation(nums))