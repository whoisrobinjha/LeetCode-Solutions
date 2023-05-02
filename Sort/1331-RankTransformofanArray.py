#LeetCode Problem 1331. Rank Transform of an Array Solution
# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr):
        self.quicksort(arr)
        rank_dict = {num: i+1 for i, num in enumerate(sorted(set(arr)))}
        return [rank_dict[num] for num in arr]

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x < pivot]
            right = [x for x in arr[1:] if x >= pivot]
            return self.quicksort(left) + [pivot] + self.quicksort(right)
    
arr = [40,10,20,30]
print(Solution().arrayRankTransform(arr))