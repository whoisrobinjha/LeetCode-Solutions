#Leetcode Problem 441 - Arranging Coins Solution
#https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = (start + end) >> 1
            coinsFilled = mid * (mid + 1) // 2
            if coinsFilled == n:
                return mid
            elif coinsFilled < n:
                start = mid + 1
            else:
                end = mid - 1
        return start - 1

print(Solution().arrangeCoins(5))