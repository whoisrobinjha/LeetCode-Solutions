#LeetCode Problem 1217 - Minimum Cost to Move Chips to The Same Position Solution
#https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)

class Solution:
    def minCostToMoveChips(self, position):
        count_even = 0
        count_odd = 0
        for i in position:
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        return min(count_even, count_odd)

position = [1,2,3]
print(Solution().minCostToMoveChips(position))