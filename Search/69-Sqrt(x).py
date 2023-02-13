#Leetcode problem 69 - Sqrt(x) solution
#https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        if(x < 2):
            return x
        start = 0
        end = int(x/2)

        while(start <= end):
            mid = (start + end) >> 1
            if(mid*mid > x):
                end = mid - 1
            else: start = mid + 1
        return end

print(Solution().mySqrt(196))