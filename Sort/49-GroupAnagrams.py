#LeetCode Problem 49. Group Anagrams Solution
#https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        grouped_anagrams = defaultdict(list)
        for word in strs:
            sorted_word = self.sort_chars(word)
            grouped_anagrams[sorted_word].append(word)
        return list(grouped_anagrams.values())

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

    def sort_chars(self, word):
        return ''.join(self.quicksort(list(word)))
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))