#LeetCode Problem 1513. Number of Substrings With Only 1s Solution
# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s):
        count = 0
        consecutive_ones = 0
        mod = 10 ** 9 + 7

        for i in s:
            if i == '1':
                consecutive_ones += 1
            else:
                consecutive_ones = 0

            count += consecutive_ones

        return count % mod