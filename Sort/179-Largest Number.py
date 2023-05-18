#LeetCode Problem 179  Largest Number Solution
# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums) -> str:
        nums = [str(num) for num in nums]
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.compare(nums[j], nums[j+1]) > 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        result = ''.join(nums)
        result = result.lstrip('0')
        return result if result else '0'

    def compare(self,x, y):
            return int(y + x) - int(x + y)
    
nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))