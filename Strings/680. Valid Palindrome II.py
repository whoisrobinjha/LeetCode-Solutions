#LeetCode Problem 680. Valid Palindrome II Solution
# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s):
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                sub1 = s[start : end]
                sub2 = s[start + 1 : end + 1]
                if sub1 == sub1[::-1] or sub2 == sub2[::-1]:
                    return True
                sub1 = s[start : end]
                sub2 = s[start : end]
                if sub1 == sub1[::-1] or sub2 == sub2[::-1]:
                    return True
                return False
            start += 1
            end -= 1
        return True

s = "abca"
print(Solution().validPalindrome(s))