# LeetCode Problem 1838 - Frequency of the Most Frequent Element Solution
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        start = 0
        sum_nums = 0
        max_freq = 1
        for end in range(len(nums)):
            sum_nums += nums[end]
            while nums[end] * (end - start + 1) - sum_nums > k:
                sum_nums -= nums[start]
                start += 1
            max_freq = max(max_freq, end - start + 1)
        return max_freq

nums = [1,2,4]
k = 5
print(Solution().maxFrequency(nums, k))