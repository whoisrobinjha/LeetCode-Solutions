#LeetCode Problem 1208. Get Equal Substrings Within Budget Solution
# https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s, t, maxCost):
        left = 0
        maxLength = 0
        currentCost = 0
        
        for right in range(len(s)):
            currentCost += abs(ord(s[right]) - ord(t[right]))
        
            if currentCost > maxCost:
                currentCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength