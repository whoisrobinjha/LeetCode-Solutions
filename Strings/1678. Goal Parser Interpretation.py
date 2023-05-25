#LeetCode Problem 1678. Goal Parser Interpretation Solution
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command):
        interpreted = ""
        i = 0

        while i < len(command):
            if command[i] == 'G':
                interpreted += 'G'
                i += 1
            elif command[i:i+2] == '()':
                interpreted += 'o'
                i += 2
            elif command[i:i+4] == '(al)':
                interpreted += 'al'
                i += 4

        return interpreted

command = "G()(al)"
print(Solution().interpret(command))