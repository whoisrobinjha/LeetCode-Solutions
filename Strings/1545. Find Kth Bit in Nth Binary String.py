#LeetCode Problem 1545. Find Kth Bit in Nth Binary String Solution
#https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n, k):
        if n == 1:
            return "0"

        length = 2 ** n - 1
        mid = length // 2 + 1

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            inverted_bit = self.findKthBit(n - 1, length - k + 1)
            return "1" if inverted_bit == "0" else "0"

        return self.findKthBit(n - 1, k)
        