#LeetCode Problem 744 - Find Smallest Letter Greater Than Target Solution
#https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

letters = ["c","f","j"]
target = "a"
print(Solution().nextGreatestLetter(letters, target))