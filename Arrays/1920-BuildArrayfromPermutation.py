#LeetCode Problem 1920 - Build Array from Permutation Solution
#https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums):
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans

nums = [0,2,1,5,3,4]
print(Solution().buildArray(nums))