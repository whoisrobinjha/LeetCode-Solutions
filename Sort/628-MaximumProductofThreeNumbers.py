#LeetCode Problem 628 - Maximum Product of Three Numbers Solution
#https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
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
        
        nums_sorted = merge_sort(nums)
        n = len(nums_sorted)
        case1 = nums_sorted[n-1] * nums_sorted[n-2] * nums_sorted[n-3]
        case2 = nums_sorted[0] * nums_sorted[1] * nums_sorted[n-1]
        return max(case1, case2)

nums = [3,6,4,8]
print(Solution().maximumProduct(nums))