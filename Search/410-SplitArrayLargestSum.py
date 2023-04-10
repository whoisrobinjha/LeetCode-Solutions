#LeetCode Problem 410 - Split Array Largest Sum Solution
# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            count = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    count += 1
                    curr_sum = num
                    if count > k:
                        break
            if count <= k:
                right = mid
            else:
                left = mid + 1
        
        return left
    
nums = [7,2,5,10,8]
k = 2
print(Solution().splitArray(nums, k))