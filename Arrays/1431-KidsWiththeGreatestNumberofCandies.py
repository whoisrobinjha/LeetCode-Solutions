#LeetCode Problem 1431 - Kids With the Greatest Number of Candies Solution
#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        max_candies = max(candies)
        for candy in candies:
            ans.append(candy + extraCandies >= max_candies)
        return ans

candies = [2,3,5,1,3]
extraCandies = 3
print(Solution().kidsWithCandies(candies, extraCandies))