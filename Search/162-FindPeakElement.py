#LeetCode Problem 162 - Find Peak Element Solution
#https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            mid = (start + end) >> 1
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start
    
nums = [1,2,3,1]
print(Solution().findPeakElement(nums))