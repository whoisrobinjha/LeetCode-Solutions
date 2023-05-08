#LeetCode Problem 645. Set Mismatch Solution
# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i+1]
        return [-1, -1]

nums = [1,2,2,4]
print(Solution().findErrorNums(nums))