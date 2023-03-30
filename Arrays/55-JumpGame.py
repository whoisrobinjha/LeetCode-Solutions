#LeetCode Problem 55. Jump Game Solution
#https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums):
        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True

nums = [2,3,1,1,4]
print(Solution().canJump(nums))