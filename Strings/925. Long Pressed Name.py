#LeetCode Problem 925. Long Pressed Name Solution
# https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name, typed):
        i, j = 0, 0
        
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False

        return i == len(name)

name = "alex"
typed = "aaleex"
print(Solution().isLongPressedName(name,typed))