#LeetCode Problem 848. Shifting Letters Solution
# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        cumulative_shift = 0
        result = [''] * n

        for i in range(n - 1, -1, -1):
            cumulative_shift += shifts[i]
            index = ord(s[i]) - ord('a')
            shifted_index = (index + cumulative_shift) % 26
            result[i] = chr(ord('a') + shifted_index)

        return ''.join(result)