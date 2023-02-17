#LeetCode Problem 704 - Binary Search Solution
#https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums, target):
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
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))