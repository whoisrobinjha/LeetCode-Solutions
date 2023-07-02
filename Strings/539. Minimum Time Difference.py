#LeetCode Problem 539. Minimum Time Difference Solution
# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints):
        timePoints = sorted(timePoints)
        min_diff = float('inf')
        for i in range(1, len(timePoints)):
            diff = self.convert_to_minutes(timePoints[i]) - self.convert_to_minutes(timePoints[i-1])
            min_diff = min(min_diff, diff)

        first_time = self.convert_to_minutes(timePoints[0])
        last_time = self.convert_to_minutes(timePoints[-1])
        circular_diff = (24 * 60) - last_time + first_time
        min_diff = min(min_diff, circular_diff)

        return min_diff

    def convert_to_minutes(self, time):
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes