#LeetCode Problem 33 - Search in Rotated Sorted Array Solution
#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, arr, target):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) >> 1
            if arr[mid] == target:
                return mid
            if arr[start] <= arr[mid]:
                if arr[start] <= target and target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if arr[mid] < target and target <= arr[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))