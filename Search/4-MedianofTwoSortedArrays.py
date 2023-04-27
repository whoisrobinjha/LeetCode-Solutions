#LeetCode Problem 4 - Median of Two Sorted Arrays Solution
#https://leetcode.com/problems/median-of-two-sorted-arrays/

import sys

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            if i < m and nums2[j-1] > nums1[i]:
                left = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                if i == 0:
                    nums1_left = -sys.maxsize-1
                else:
                    nums1_left = nums1[i-1] 
                if i == m:
                    nums1_right = sys.maxsize
                else:
                    nums1_right = nums1[i]  
                if j == 0:
                    nums2_left = -sys.maxsize-1
                else:
                    nums2_left = nums2[j-1] 
                if j == n:
                    nums2_right = sys.maxsize
                else:
                    nums2_right = nums2[j]
                if (m + n) % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return max(nums1_left, nums2_left)

nums1 = [1,3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))