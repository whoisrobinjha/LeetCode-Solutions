# LeetCode Problem 448. Find All Numbers Disappeared in an Array Solution
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        while i < n:
            if nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        missing_numbers = []
        for i in range(n):
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
        
        return missing_numbers

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))