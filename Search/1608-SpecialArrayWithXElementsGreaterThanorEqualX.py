#Leetcode Problem 1608 - Special Array With X Elements Greater Than or Equal X Solution
#https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums):
        nums.sort(reverse=True)
        start = 0
        end = len(nums)
        while start <= end:
            mid = (start + end) >> 1
            count = sum(1 for num in nums if num >= mid)
            if count == mid:
                return mid
            elif count < mid:
                end = mid - 1
            else:
                start = mid + 1
        return -1

nums = [3,5]
print(Solution().specialArray(nums))