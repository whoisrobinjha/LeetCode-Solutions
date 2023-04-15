#LeetCode Problem 217 - Contains Duplicate Solution
#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))