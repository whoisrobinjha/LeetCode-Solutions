#LeetCode Problem 1967. Number of Strings That Appear as Substrings in Word Solution
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns, word):
        return sum(pattern in word for pattern in patterns)

patterns = ["a","abc","bc","d"]
word = "abc"
print(Solution().numOfStrings(patterns, word))