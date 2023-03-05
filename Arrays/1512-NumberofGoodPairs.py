#LeetCode Problem 1512 - Number of Good Pairs Solution
#https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums):
        freq = {}
        count = 0
        for num in nums:
            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        return count
    
nums = [1,2,3,1,1,3]
print(Solution().numIdenticalPairs(nums))