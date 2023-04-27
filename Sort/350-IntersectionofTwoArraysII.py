#LeetCode Problem 350 - Intersection of Two Arrays II Solution
#https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        intersect_set = set(nums1) & set(nums2)
        result = []
        
        for num in intersect_set:
            result.extend([num] * min(count1[num], count2[num]))
        return result

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))