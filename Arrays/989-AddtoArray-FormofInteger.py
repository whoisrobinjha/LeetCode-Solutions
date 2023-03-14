#LeetCode Problem 989. Add to Array-Form of Integer Solution
#https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num, k):
        carry = 0
        i = len(num) - 1
        result = []
        while k or i >= 0:
            if i >= 0:
                carry += num[i]
            if k:
                carry += k % 10
                k //= 10
            result.append(carry % 10)
            carry //= 10
            i -= 1
        if carry:
            result.append(carry)
        return result[::-1]
    
num = [1,2,0,0]
k = 34
print(Solution().addToArrayForm(num, k))