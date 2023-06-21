#LeetCode Problem 1813. Sentence Similarity III Solution
# https://leetcode.com/problems/sentence-similarity-iii/

class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        if len(sentence1) < len(sentence2): 
            sentence1, sentence2 = sentence2, sentence1 
            
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        lo = 0 
        while lo < len(words2) and words1[lo] == words2[lo]: lo += 1
        
        hi = -1 
        while -len(words2) <= hi and words1[hi] == words2[hi]: hi -= 1
        
        return lo - hi -1 >= len(words2)