#LeetCode Problem 215. Kth Largest Element in an Array Solution
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import random

class Solution:
    def findKthLargest(self, nums, k):
        target_index = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, target_index)
    
    def quickSelect(self, nums, start, end, target_index):
        pivot_index = random.randint(start, end)
        pivot = nums[pivot_index]
        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
        partition_index = start

        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[partition_index] = nums[partition_index], nums[i]
                partition_index += 1
        
        nums[partition_index], nums[end] = nums[end], nums[partition_index]
        
        if partition_index == target_index:
            return nums[partition_index]
        elif partition_index < target_index:
            return self.quickSelect(nums, partition_index + 1, end, target_index)
        else:
            return self.quickSelect(nums, start, partition_index - 1, target_index)

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))