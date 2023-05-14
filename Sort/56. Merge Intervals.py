#LeetCode Problem 56. Merge Intervals Solution
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = []
        for interval in sorted_intervals:
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        return merged_intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))