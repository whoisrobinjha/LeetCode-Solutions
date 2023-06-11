#LeetCode Problem 1668. Maximum Repeating Substring Solution
# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence, word):
        max_k = 0
        k = 1
        while word * k in sequence:
            max_k = k
            k += 1

        return max_k

sequence = "ababc"
word = "ab"
print(Solution().maxRepeating(sequence, word))