#LeetCode Problem 1 - Two Sum Solution
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        nums_sorted = nums.copy()
        self.quicksort(nums_sorted, 0, n-1)
        left, right = 0, n - 1
        while left < right:
            sum = nums_sorted[left] + nums_sorted[right]
            if sum == target:
                index1 = nums.index(nums_sorted[left])
                index2 = nums.index(nums_sorted[right])
                if index1 == index2:
                    index2 = nums[index1+1:].index(nums_sorted[right]) + index1 + 1
                return [index1, index2]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return []
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    def quicksort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quicksort(arr, low, pi-1)
            self.quicksort(arr, pi+1, high)

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))