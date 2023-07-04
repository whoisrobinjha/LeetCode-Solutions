#LeetCode Problem 1023. Camelcase Matching Solution
# https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries, pattern):  
        return [self.is_match(query, pattern) for query in queries]
    
    def is_match(self, query, pattern):
        i = j = 0
        while i < len(query) and j < len(pattern):
            if query[i] == pattern[j]:
                i += 1
                j += 1
            elif query[i].islower():
                i += 1
            else:
                return False
        
        if i < len(query):
            return all(char.islower() for char in query[i:])
        
        return j == len(pattern)