#LeetCode Problem 224. Basic Calculator Solution
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s):
        s = s.replace(" ", "")
        stack = []
        operand = 0
        sign = 1
        result = 0
        for char in s:
            if char.isdigit():
                operand = (operand * 10) + int(char)
            elif char == '+':
                result += sign * operand
                operand = 0
                sign = 1
            elif char == '-':
                result += sign * operand
                operand = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * operand
                operand = 0
                result *= stack.pop()
                result += stack.pop()
        return result + (sign * operand)