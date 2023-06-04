#LeetCode Problem  168. Excel Sheet Column Title Solution
# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            letter = chr(ord('A') + remainder)
            result = letter + result
            columnNumber //= 26
        return result

columnNumber = 28
print(Solution().convertToTitle(columnNumber))