#LeetCode Problem 238 - Product of Array Except Self Solution
#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n
        answer = [1] * n
        for i in range(1, n):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i+1]
        for i in range(n):
            answer[i] = prefixProduct[i] * suffixProduct[i]
        
        return answer

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))