#LeetCode Problem 154 - Find Minimum in Rotated Sorted Array II Solution
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
    
nums = [2,2,2,0,1]
print(Solution().findMin(nums))