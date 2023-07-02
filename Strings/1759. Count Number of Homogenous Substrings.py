#LeetCode Problem 1759. Count Number of Homogenous Substrings Solution
# https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s):
        count = 0
        current_char = ''
        current_count = 0
        mod = 10**9 + 7

        for char in s:
            if char == current_char:
                current_count += 1
            else:
                count += (current_count * (current_count + 1)) // 2
                current_char = char
                current_count = 1

        count += (current_count * (current_count + 1)) // 2
        return count % mod