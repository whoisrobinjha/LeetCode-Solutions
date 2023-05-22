#LeetCode Problem 41. First Missing Positive Solution
# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

nums = [3,4,-1,1]
print(Solution().firstMissingPositive(nums))