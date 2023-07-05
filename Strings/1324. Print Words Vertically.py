#LeetCode Problem 1324. Print Words Vertically Solution
#https://leetcode.com/problems/print-words-vertically/

class Solution:
    def printVertically(self, s):
        words = s.split()
        max_length = max(len(word) for word in words)
        result = [''] * max_length

        for word in words:
            for i in range(max_length):
                if i < len(word):
                    result[i] += word[i]
                else:
                    result[i] += ' '

        return [word.rstrip() for word in result]