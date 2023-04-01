#LeetCode Problem 189 - Rotate Array Solution
#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k))