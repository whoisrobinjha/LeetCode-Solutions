#LeetCode Problem 859. Buddy Strings Solution
# https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(s) - len(set(s)) >= 1
        
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
            if len(diff) > 2:
                return False
            
        if len(diff) != 2:
            return False
        
        if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True
    
        return False

s = "ab"
goal = "ab"
print(Solution().buddyStrings(s, goal))