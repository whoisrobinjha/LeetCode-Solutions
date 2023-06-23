#LeetCode Problem 556. Next Greater Element III Solution
# https://leetcode.com/problems/next-greater-element-iii/

class Solution:
    def nextGreaterElement(self, n):
        digits = list(str(n))
    
        pivot_idx = len(digits) - 2
        while pivot_idx >= 0 and digits[pivot_idx] >= digits[pivot_idx + 1]:
            pivot_idx -= 1
        
        if pivot_idx == -1:
            return -1
        
        successor_idx = len(digits) - 1
        while digits[successor_idx] <= digits[pivot_idx]:
            successor_idx -= 1
        
        digits[pivot_idx], digits[successor_idx] = digits[successor_idx], digits[pivot_idx]
        digits[pivot_idx + 1:] = reversed(digits[pivot_idx + 1:])
        
        result = int(''.join(digits))
        
        if result > 2**31 - 1:
            return -1
        
        return result