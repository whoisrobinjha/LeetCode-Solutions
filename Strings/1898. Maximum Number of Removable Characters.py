#LeetCode Problem 1898. Maximum Number of Removable Characters Solution
# https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution:
    def maximumRemovals(self, s, p, removable):
        left = 0
        right = len(removable) - 1

        while left <= right:
            mid = (left + right) >> 1
            s_mod = list(s)
            for i in range(mid + 1):
                s_mod[removable[i]] = ''

            if self.isSubsequence(''.join(s_mod), p):
                left = mid + 1
            else:
                right = mid - 1

        return right + 1

    def isSubsequence(self, s, p):
        i = j = 0
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                j += 1
            i += 1
        return j == len(p)