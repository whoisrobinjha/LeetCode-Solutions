#LeetCode Problem 540 - Single Element in a Sorted Array Solution
#https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) >> 1
            if mid % 2 == 0:
                if nums[mid] ==  nums[mid + 1]:
                    start = mid + 2
                else:
                    end = mid 
            else:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return nums[start]

nums = [1,1,2,2,3,3,4,8,8]
print(Solution().singleNonDuplicate(nums))