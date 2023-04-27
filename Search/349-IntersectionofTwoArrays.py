#Leetcode Problem 349 - Intersection of Two Arrays Solution
#https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1, nums2):
        temp_set1 = set(nums1)
        temp_set2 = set(nums2)
        return list(temp_set1 & temp_set2)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))