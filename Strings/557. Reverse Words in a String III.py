#LeetCode Problem 557. Reverse Words in a String III Solution
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))

s = "God Ding"
print(Solution().reverseWords(s))