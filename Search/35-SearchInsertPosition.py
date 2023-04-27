#LeetCode Problem 35 - Search Insert Position Solution
#https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return start

arr = [1,3,5,6]
target = 7
print(Solution().searchInsert(arr, target))