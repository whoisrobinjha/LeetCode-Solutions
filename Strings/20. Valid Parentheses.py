#LeetCode Problem 20. Valid Parentheses Solution
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in brackets:
                stack.append(i)
            elif not stack or brackets[stack.pop()] != i:
                return False
        return not stack