#LeetCode Problem 922. Sort Array By Parity II Solution
#https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums):
        even_index = 0
        odd_index = 1
        n = len(nums)
        ans = [None] * n
        for i in range(n):
            if nums[i] % 2 == 0:
                ans[even_index] = nums[i]
                even_index += 2
            else:
                ans[odd_index] = nums[i]
                odd_index += 2
        return ans

nums = [4,2,5,7]
print(Solution().sortArrayByParityII(nums))