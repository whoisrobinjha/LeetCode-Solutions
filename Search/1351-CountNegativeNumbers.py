#Leetcode problem 1351 - Count Negative Numbers in a Sorted Matrix
#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

class Solution:
    def count_negatives(self,grid):
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            passed_list = grid[i]
            first_occurance = self.first_negative(passed_list)
            count += n - first_occurance
        return count

    def first_negative(self,grid):
        start = 0
        end = len(grid) - 1
        fNegative = len(grid)
        while start <= end:
            mid = (start + end) >> 1
            if grid[mid] < 0:
                fNegative = mid
                end = mid - 1
            else:
                start = mid + 1
        return fNegative

grid = [list(range(340,-1505400,-1)), list(range(125,-40054,-2)), list(range(-125,-8545,-5))]
print(Solution().count_negatives(grid))
