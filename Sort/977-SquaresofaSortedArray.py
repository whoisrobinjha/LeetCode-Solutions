#LeetCode Problem 977. Squares of a Sorted Array Solution
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):       
        squared_nums = [num ** 2 for num in nums]
        return self.merge_sort(squared_nums)
    
    def merge(self, left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            return result
        
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) >> 1
        left = nums[:mid]
        right = nums[mid:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)

nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))