#LeetCode Problem 14. Longest Common Prefix Solution
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            if any(string[i] != char for string in strs):
                return shortest[:i]

        return shortest

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))