#LeetCode Problem 1389 - Create Target Array in the Given Order Solution
#https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
    
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(Solution().createTargetArray(nums, index))