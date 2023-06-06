#LeetCode Problem 28. Find the Index of the First Occurrence in a String Solution
# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)
    
haystack = "sadbutsad"
needle = "sad"
print(Solution().strStr(haystack, needle))