#LeetCode Problem 1539 - Kth Missing Positive Number Solution
#https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr, k):
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (start + end) >> 1
            if arr[mid] - mid - 1 < k:
                start = mid + 1 
            else:
                end = mid - 1
        return start + k

arr = [2,3,4,7,11]
k = 5
print(Solution().findKthPositive(arr, k))