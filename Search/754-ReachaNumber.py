#LeetCode Problem 754 - Reach a Number Solution
#https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        start = 0
        end = float('inf')
        while start < end:
            mid = (start + end) >> 1
            total_distance = mid * (mid + 1) // 2
            if total_distance >= target and (total_distance - target) % 2 == 0:
                end = mid
            else:
                start = mid + 1
        return start