#LeetCode Problem 1616. Split Two Strings to Make Palindrome Solution
# https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def checkPalindromeFormation(self, a, b):
        n = len(a)
        start = 0
        end = n - 1
        while start < end and a[start] == b[end]:
            start += 1
            end -= 1
        if self.isPalindrome(a, start, end) or self.isPalindrome(b, start, end):
            return True
        start = 0
        end = n - 1
        while start < end and b[start] == a[end]:
            start += 1
            end -= 1
        if self.isPalindrome(b, start, end) or self.isPalindrome(a, start, end):
            return True
        return False

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True