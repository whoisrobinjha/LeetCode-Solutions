#LeetCode Problem 1464. Maximum Product of Two Elements in an Array Solution
#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)
        return (nums[0]-1) * (nums[1]-1)

    def quicksort(self, nums, start, end):
        if start >= end:
            return
        pivot_index = self.partition(nums, start, end)
        self.quicksort(nums, start, pivot_index - 1)
        self.quicksort(nums, pivot_index + 1, end)

    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start - 1
        for j in range(start, end):
            if nums[j] >= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[end] = nums[end], nums[i+1]
        return i+1

nums = [3,4,5,2]
print(Solution().maxProduct(nums))