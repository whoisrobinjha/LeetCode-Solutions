#LeetCode Problem 1784. Check if Binary String Has at Most One Segment of Ones Solution
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                if i == 0 or s[i - 1] == '0':
                    count += 1
                if count > 1:
                    return False
        return True