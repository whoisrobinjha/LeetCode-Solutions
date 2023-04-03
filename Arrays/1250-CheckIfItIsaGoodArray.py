#LeetCode Problem 1250. Check If It Is a Good Array Solution
#https://leetcode.com/problems/check-if-it-is-a-good-array/

import math

class Solution:
    def isGoodArray(self, nums) -> bool:
        return math.gcd(*nums) == 1

nums = [12,5,7,23]
print(Solution().isGoodArray(nums))