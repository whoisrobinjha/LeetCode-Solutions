# LeetCode Problem 686. Repeated String Match Solution
# https://leetcode.com/problems/repeated-string-match/

class Solution:
    def repeatedStringMatch(self, a, b):
        count = 1
        repeated = a
        
        while len(repeated) < len(b):
            repeated += a
            count += 1

        if b in repeated:
            return count

        repeated += a
        count += 1

        if b in repeated:
            return count

        return -1