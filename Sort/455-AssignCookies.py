#LeetCode Problem 455 - Assign Cookies Solution
#https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i, j, count = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count

g = [1,2,3]
s = [1,1]
print(Solution().findContentChildren(g,s))