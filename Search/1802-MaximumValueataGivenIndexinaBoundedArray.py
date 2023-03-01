#LeetCode Problem 1802 - Maximum Value at a Given Index in a Bounded Array Solution
#https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution:
    def maxValue(self, n, index, maxSum):
        start = 1
        end = maxSum - n + 1
        
        while start <= end:
            mid = (start + end) >> 1
            total = mid
            left_sum = mid - 1
            right_sum = mid - 1
            
            for i in range(1, index + 1):
                if left_sum > 0:
                    total += min(mid - 1, left_sum)
                    left_sum -= 1
                    
            for i in range(index + 1, n):
                if right_sum > 0:
                    total += min(mid - 1, right_sum)
                    right_sum -= 1
                    
            if total > maxSum:
                end = mid - 1
            else:
                start = mid + 1
        
        return end
    
n = 4
index = 2
maxSum = 6
print(Solution().maxValue(n, index, maxSum))