#LeetCode Problem 1200. Minimum Absolute Difference Solution
# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr):     
        self.quick_sort(arr, 0, len(arr)-1)
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff < min_diff:
                min_diff = diff
        pairs = []
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == min_diff:
                pairs.append([arr[i-1], arr[i]])
        return pairs

    def quick_sort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quick_sort(arr, low, pivot - 1)
            self.quick_sort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

arr = [4,2,1,3]
print(Solution().minimumAbsDifference(arr))