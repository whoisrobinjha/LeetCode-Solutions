#LeetCode Problem 198 - House Robber Solution
#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[n-1]
    
nums = [1,2,3,1]
print(Solution().rob(nums))