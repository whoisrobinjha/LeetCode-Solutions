#LeetCode Problem 34 - Find First and Last Position of Element in Sorted Array Solution
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self,nums, target):
        return [self.findFirstOccurrence(nums, target), self.findLastOccurrence(nums, target)]
              
    def findFirstOccurrence(self,nums, target):
        left, right = 0, len(nums) - 1
        firstOccurrence = -1
        while left <= right:
            middle = (right + left) >> 1
            if target == nums[middle]:
                firstOccurrence = middle
                right = middle - 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return firstOccurrence
    
    def findLastOccurrence(self,nums, target):
        left, right = 0, len(nums) - 1
        lastOccurrence = -1
        while left <= right:
            middle = (right + left) >> 1
            if target == nums[middle]:
                lastOccurrence = middle
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return lastOccurrence

nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))