#LeetCode Problem 1 - Two Sum Solution
#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))