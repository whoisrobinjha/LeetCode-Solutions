#LeetCode Problem 287. Find the Duplicate Number Solution
# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums):
        start = 1
        end = len(nums) - 1
        while start < end:
            mid = (start + end) >> 1
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                start = mid + 1
            else:
                end = mid
        return start

nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))