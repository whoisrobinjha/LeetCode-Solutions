#LeetCode Problem 1163. Last Substring in Lexicographical Order Solution
# https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution:
    def lastSubstring(self, s):
        current_max_char = ''
        current_max_substr = ''
        
        for i in range(len(s)):
            if s[i] > current_max_char:
                current_max_char = s[i]
                current_max_substr = s[i:]
            elif s[i] == current_max_char:
                current_max_substr = max(current_max_substr, s[i:])
        
        return current_max_substr