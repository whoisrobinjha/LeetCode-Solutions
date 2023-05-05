#LeetCode Problem 1636 - Sort Array by Increasing Frequency Solution
#https://leetcode.com/problems/sort-array-by-increasing-frequency/


from collections import Counter
class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)
        sorted_count = sorted(count.items(), key=lambda x: (x[1], -x[0]))
        result = []
        for item in sorted_count:
            result += [item[0]] * item[1]
        return result
    
nums = [1,1,2,2,2,3]
print(Solution().frequencySort(nums))