#LeetCode Peoblem 287. Find the Duplicate Number Solution
# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i]
            else:
                i += 1
        return -1 

nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))