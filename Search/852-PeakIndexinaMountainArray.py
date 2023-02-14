#LeetCode Problem 852 - Peak Index in a Mountain Array Solution
#https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = (start + end) >> 1
            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start

arr = [0,2,1,0]
print(Solution().peakIndexInMountainArray(arr))
