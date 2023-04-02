#LeetCode Problem 198 - House Robber Solution
#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        robbed_yes = 0
        robbed_no = 0
        
        for i in range(len(nums)):
            current_robbed = robbed_no + nums[i]
            current_not_robbed = max(robbed_yes, robbed_no)
            
            robbed_yes = current_robbed
            robbed_no = current_not_robbed
            
        return max(robbed_yes, robbed_no)
    
nums = [1,2,3,1]
print(Solution().rob(nums))