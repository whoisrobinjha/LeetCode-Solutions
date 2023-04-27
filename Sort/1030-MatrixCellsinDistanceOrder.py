#LeetCode Problem 1030. Matrix Cells in Distance Order Solution
# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        distances = []
        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                distances.append((distance, [r, c]))
        
        self.quicksort(distances)
        
        return [coord for distance, coord in distances]

    def partition(self, array, low, high):
        pivot = array[high][0]
        i = low - 1
        for j in range(low, high):
            if array[j][0] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    def quicksort(self, array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = self.partition(array, low, high)
            self.quicksort(array, low, pivot_index - 1)
            self.quicksort(array, pivot_index + 1, high)

rows = 2
cols = 2
rCenter = 0
cCenter = 1
print(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter))