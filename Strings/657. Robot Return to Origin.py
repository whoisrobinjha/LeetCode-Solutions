#LeetCode Problem 657. Robot Return to Origin Solution
# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves):
        x = 0
        y = 0

        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1

        return x == 0 and y == 0

moves = "UD"
print(Solution().judgeCircle(moves))