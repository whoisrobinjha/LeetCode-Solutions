# LeetCode Problem 448. Find All Numbers Disappeared in an Array Solution
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]

        missing_numbers = []
        for i in range(n):
            if nums[i] > 0:
                missing_numbers.append(i + 1)
            
        return missing_numbers

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))