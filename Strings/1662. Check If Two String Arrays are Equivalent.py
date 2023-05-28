#LeetCode Problem 1662. Check If Two String Arrays are Equivalent Solution
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(Solution().arrayStringsAreEqual(word1, word2))