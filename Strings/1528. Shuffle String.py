#LeetCode Problem 1528. Shuffle String Solution
# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices):
        shuffled = [''] * len(s)
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
        return ''.join(shuffled)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(Solution().restoreString(s, indices))