#LeetCode Problem 888 - Fair Candy Swap Solution
#https://leetcode.com/problems/fair-candy-swap/description/

class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)
        diff = (total_alice - total_bob) // 2
        set_bob = set(bobSizes)
        for size in aliceSizes:
            if size - diff in set_bob:
                return [size, size - diff]
        return []

aliceSizes = [1,1]
bobSizes = [2,2]
print(Solution().fairCandySwap(aliceSizes, bobSizes))