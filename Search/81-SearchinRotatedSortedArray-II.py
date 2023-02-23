#LeetCode Problem 81 - Search in Rotated Sorted Array II Solution
#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) >> 1
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        pivot = start
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) >> 1
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] == target:
                return True
            elif nums[mid_pivot] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return False
        
nums = [2,5,6,0,0,1,2]
target = 2
print(Solution().search(nums, target))