#LeetCode Problem 41 - First Missing Positive Solution
#https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, arr):
        i = 0
        while i < len(arr):
            correct = arr[i] - 1
            if 0 < arr[i] <= len(arr) and arr[i] != arr[correct]:
                self.swap(arr, i, correct)
            else:
                i += 1
        for index in range(len(arr)):
            if arr[index] != index + 1:
                return index + 1
        return len(arr) + 1

    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp

nums = [1,2,0]
print(Solution().firstMissingPositive(nums))