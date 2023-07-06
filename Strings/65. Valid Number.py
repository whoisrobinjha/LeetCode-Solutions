#LeetCode Problem 65. Valid Number Solution
# https://leetcode.com/problems/valid-number/

class Solution:
    def isNumber(self, s):
        s = s.strip()
        n = len(s)
        digitSeen = False
        dotSeen = False
        eSeen = False

        for i in range(n):
            c = s[i]

            if c.isdigit():
                digitSeen = True
            elif c == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif c.lower() == 'e':
                if eSeen or not digitSeen:
                    return False
                eSeen = True
                digitSeen = False
            elif c in ('+', '-'):
                if i != 0 and s[i - 1].lower() != 'e':
                    return False
            else:
                return False

        return digitSeen and (not eSeen or digitSeen) and (not dotSeen or digitSeen)