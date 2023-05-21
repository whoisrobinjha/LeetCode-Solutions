#LeetCode Problem 442. Find All Duplicates in an Array Solution
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums):
        n = len(nums)
        i = 0
        duplicates = []

        while i < n:
            num = nums[i]
            if num == i + 1:
                i += 1
            elif nums[num - 1] == num:
                if num not in duplicates:
                    duplicates.append(num)
                i += 1
            else:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]

        return duplicates

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(nums))