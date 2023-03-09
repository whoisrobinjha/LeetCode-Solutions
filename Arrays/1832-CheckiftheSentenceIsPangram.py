#LeetCode Problem 1832 - Check if the Sentence Is Pangram Solution
#https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        return set(sentence.lower()) >= alphabet

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(Solution().checkIfPangram(sentence))