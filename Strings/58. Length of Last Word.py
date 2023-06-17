#LeetCode Problem 58. Length of Last Word Solution
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s):
        words = s.split()
        words = words[::-1]
        return len(words[0])