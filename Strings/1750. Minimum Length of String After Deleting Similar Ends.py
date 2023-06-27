#LeetCode Problem 1750. Minimum Length of String After Deleting Similar Ends Solution
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s):
        start = 0
        end = len(s) - 1

        while start < end and s[start] == s[end]:
            ch = s[start]
            while start <= end and s[start] == ch:
                start += 1
            while start < end and s[end] == ch:
                end -= 1

        return end - start + 1