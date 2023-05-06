#LeetCode Problem 1608 - Special Array With X Elements Greater Than or Equal X Solution
#https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

class Solution:
    def specialArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        start = 0
        end = len(nums)
        while start <= end:
            mid = (start + end) >> 1
            count = sum(1 for num in nums if num >= mid)
            if count == mid:
                return mid
            elif count < mid:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    def quickSort(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot - 1)
            self.quickSort(nums, pivot + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] >= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1

nums = [0,4,3,0,4]
print(Solution().specialArray(nums))