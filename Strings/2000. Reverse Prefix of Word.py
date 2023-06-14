#LeetCode Problem 2000. Reverse Prefix of Word Solution
# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word

        index = word.index(ch)
        reversed_segment = word[:index+1][::-1]
        return reversed_segment + word[index+1:]