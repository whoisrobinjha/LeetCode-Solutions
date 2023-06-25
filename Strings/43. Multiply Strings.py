#LeetCode Problem 43. Multiply Strings Solution
# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            carry = 0
            d1 = int(num1[i])
            for j in range(len(num2)):
                d2 = int(num2[j])
                product = (d1 * d2) + carry
                digit = product % 10
                carry = product // 10
                result[i + j] += digit
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

            if carry > 0:
                result[i + len(num2)] += carry

        result = result[::-1]
        result = [str(digit) for digit in result]
        return ''.join(result).lstrip('0')