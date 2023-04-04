#LeetCode Problem 1818 - Minimum Absolute Sum Difference Solution
#https://leetcode.com/problems/minimum-absolute-sum-difference/

import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):
        abs_diff = sum(abs(nums1[i] - nums2[i]) for i in range(len(nums1)))
        sorted_nums1 = sorted(nums1)
        min_diff = abs_diff
        for i in range(len(nums2)):
            closest = bisect.bisect_left(sorted_nums1, nums2[i])
            if closest == len(sorted_nums1):
                closest -= 1
            elif closest > 0 and nums2[i] - sorted_nums1[closest-1] < sorted_nums1[closest] - nums2[i]:
                closest -= 1
            new_abs_diff = abs_diff - abs(nums1[i] - nums2[i]) + abs(sorted_nums1[closest] - nums2[i])
            min_diff = min(min_diff, new_abs_diff)
        return min_diff % (10**9 + 7)

nums1 = [1,10,4,4,2,7]
nums2 = [9,3,5,1,7,4]
print(Solution().minAbsoluteSumDiff(nums1, nums2))