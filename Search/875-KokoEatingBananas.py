#LeetCode Problem 875 - Koko Eating Bananas Solution
#https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:
    def minEatingSpeed(self, piles, h):
        start = 1
        end = max(piles)
        while start < end:
            mid = (start + end) >> 1
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                end = mid
            else:
                start = mid + 1
        return end

piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))