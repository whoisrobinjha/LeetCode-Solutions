#LeetCode Problem 976 - Largest Perimeter Triangle Solution
#https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums):
        nums = self.quick_sort(nums)
        for i in range(len(nums)-1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0
    
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]
            left = []
            right = []
            for i in range(1, len(nums)):
                if nums[i] < pivot:
                    left.append(nums[i])
                else:
                    right.append(nums[i])
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)

nums = [1,2,1,10]
print(Solution().largestPerimeter(nums))