#LeetCode Problem 268 - Missing Number Solution
#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums):
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] < n and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n

nums = [3,0,1]
print(Solution().missingNumber(nums))