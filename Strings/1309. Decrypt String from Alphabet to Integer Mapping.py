#LeetCode Problem 1309. Decrypt String from Alphabet to Integer Mapping Solution
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s):
        result = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                num = int(s[i:i+2])
                result += chr(num + 96)
                i += 3
            else:
                num = int(s[i])
                result += chr(num + 96)
                i += 1
        return result

s = "1326#"
print(Solution().freqAlphabets(s))