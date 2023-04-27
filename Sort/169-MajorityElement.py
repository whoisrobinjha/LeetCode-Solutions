#LeetCode Problem 169. Majority Element Solution
#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums):
        majority = 0
        count = 0
        
        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
                
        return majority

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))