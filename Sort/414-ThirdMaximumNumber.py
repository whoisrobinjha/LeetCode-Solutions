#LeetCode Problem 414 - Third Maximum Number Solution
#https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums):
        s = set()
        for num in nums:
            s.add(num)
            if len(s) > 3:
                s.remove(min(s))
        if len(s) == 3:
            return min(s)
        else:
            return max(s)
    
nums = [3,2,1]
print(Solution().thirdMax(nums))