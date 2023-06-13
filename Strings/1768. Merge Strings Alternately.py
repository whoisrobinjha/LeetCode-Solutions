#LeetCode Problem 1768. Merge Strings Alternately Solution
# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1, word2):
        merged = ""
        len1 = len(word1)
        len2 = len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                merged += word1[i]
            if i < len2:
                merged += word2[i]
        merged += word1[len1:] + word2[len2:]
        return merged