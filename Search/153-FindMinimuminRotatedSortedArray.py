#LeetCode Problem 153 - Find Minimum in Rotated Sorted Array Solution
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) >> 1
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]
        
nums = [3,4,5,0,1,2]
print(Solution().findMin(nums))