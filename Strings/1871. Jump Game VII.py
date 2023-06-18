#LeetCode Problem 1871. Jump Game VII Solution
# https://leetcode.com/problems/jump-game-vii/

class Solution:
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        pre = 0
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                pre += 1
            if i > maxJump and dp[i - maxJump - 1]:
                pre -= 1
            dp[i] = pre > 0 and s[i] == '0'

        return dp[n - 1]