# LeetCode Problem 13. Roman to Integer Solution
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        prev_value = 0
        
        for char in s:
            value = roman[char]
            if value > prev_value:
                num += value - 2 * prev_value
            else:
                num += value
            prev_value = value
        
        return num