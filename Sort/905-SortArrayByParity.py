#LeetCode Problem 905. Sort Array By Parity Solution
#https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1       
        return nums

nums = [3,1,2,4]
print(Solution().sortArrayByParity(nums))