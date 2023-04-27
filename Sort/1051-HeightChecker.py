#LeetCode Problem 1051 - Height Checker Solution
#https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights):
        sorted_heights = self.quick_sort(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count
    
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x <= pivot]
            right = [x for x in arr[1:] if x > pivot]
            return self.quick_sort(left) + [pivot] + self.quick_sort(right)
    
heights = [1,1,4,2,1,3]
print(Solution().heightChecker(heights))