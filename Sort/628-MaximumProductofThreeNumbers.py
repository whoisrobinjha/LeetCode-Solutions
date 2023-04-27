#LeetCode Problem 628 - Maximum Product of Three Numbers Solution
#https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums):
        nums_sorted = self.merge_sort(nums)
        n = len(nums_sorted)
        case1 = nums_sorted[n-1] * nums_sorted[n-2] * nums_sorted[n-3]
        case2 = nums_sorted[0] * nums_sorted[1] * nums_sorted[n-1]
        return max(case1, case2)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

nums = [3,6,4,8]
print(Solution().maximumProduct(nums))