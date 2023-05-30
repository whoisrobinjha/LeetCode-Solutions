#LeetCode Problem 1704. Determine if String Halves Are Alike Solution
#https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s):
        vowels = set('aeiouAEIOU')
        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]
        count_a = sum(1 for c in a if c in vowels)
        count_b = sum(1 for c in b if c in vowels)
        return count_a == count_b

s = "book"
print(Solution().halvesAreAlike(s))