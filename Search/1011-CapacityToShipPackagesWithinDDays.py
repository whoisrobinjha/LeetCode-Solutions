#LeetCode Problem 1011 - Capacity To Ship Packages Within D Days Solution
#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights, days):
        minCapacity = max(weights)
        maxCapacity = sum(weights)

        while minCapacity <= maxCapacity:
            midCapacity = (minCapacity + maxCapacity) >> 1
            currCapacity = 0
            currDays = 1
            for weight in weights:
                if currCapacity + weight > midCapacity:
                    currCapacity = weight
                    currDays += 1
                else:
                    currCapacity += weight
            if currDays <= days:
                maxCapacity = midCapacity - 1
            else:
                minCapacity = midCapacity + 1
                
        return minCapacity

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days))