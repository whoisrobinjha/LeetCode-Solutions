#LeetCode Problem 227. Basic Calculator II Solution
# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s):
        if s is None or len(s) == 0:
            return 0
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0

        return sum(stack)