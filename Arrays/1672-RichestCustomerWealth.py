#LeetCode Problem 1672 - Richest Customer Wealth Solution
#https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts):
        ans = 0
        for person in range(len(accounts)):
            sum = 0
            for account in range(len(accounts[person])):
                sum += accounts[person][account]
            if sum > ans:
                ans = sum
        return ans

accounts = [[1,2,3],[3,2,1]]
print(Solution().maximumWealth(accounts))